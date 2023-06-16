"""
pyenv activate py3.11_virtualenv_test
"""
import os
import io
import json
import gradio as gr
# 判断mac还是linux系统
import platform
import time
import datetime
import subprocess
if platform.system() == 'Darwin':
    yx_debug = True
elif platform.system() == 'Linux':
    yx_debug = False

if not yx_debug:
    import modules.scripts as scripts
    from modules import script_callbacks
    from modules.shared import opts
    from modules.paths import models_path

    from basicsr.utils.download_util import load_file_from_url


# class Script(scripts.Script):
#   def __init__(self) -> None:
#     super().__init__()

#   def title(self):
#     return "OpenPose Editor"

#   def show(self, is_img2img):
#     return scripts.AlwaysVisible

#   def ui(self, is_img2img):
#     return ()


def welcome(name):
    # print(1111)
    # print(os.system("ls -l"))
    return f"Welcome to Gradio, {name}!"


if 1:  # 日志获取
    getlog_js = """
function(){
    var link = document.getElementById('yxyxyx_viewlog_hreda111');
    var currentHost = window.location.host;
    var currentProtocol = window.location.protocol;
    link.href = currentProtocol + '//' + currentHost + '/psuperfaa/getlog'; //'http://localhost:7860'
}
"""

    gundongttiao_js = """
function(){
    // 等待1秒执行, 因为btn.click(fn=get_sd_log, _js=gundongttiao_js) fn和_js是一起执行的, fn还没有返回日志的时候，_js无法获取到真实高度
    setTimeout(function(){
        var logContainer = document.getElementById("logContainer");
        console.log(11111, logContainer.scrollHeight);
        logContainer.scrollTop = logContainer.scrollHeight;
    }, 1000);
}
"""

    def get_sd_log():
        if yx_debug:
            return "test log"
        else:
            log = """ <div id="logContainer" style="height: 400px; width:100%; background-color: #f2f2f2; overflow-y: scroll;"> """
            # 取文件sd.log的最后300行
            filepath = "./sd.log"
            # 判断文件是否存在
            if not os.path.exists(filepath):
                filepath = "/var/log/sdwebui/sd.log"
                if not os.path.exists(filepath):
                    filepath = "/var/log/sdwebui.log"
                    if not os.path.exists(filepath):
                        return "sd.log文件不存在"
            count = 300
            with open(filepath, "r") as f:
                lines = f.readlines()
                lines = lines[-count:]
                lines = "<br/>".join(lines)
            log += lines
            log += "</div>"
            return log

if 1:  # 保活:  会导致前端页面报错 Uncaught (in promise) TypeError: Cannot read ，但不影响啥
    get_window_url_params = """
function(keep_alive_minutes) {
    // 先清理先前的循环任务--windown.var表示全局变量
    if (typeof window.yxyxyx_kam_intervalId !== "undefined") {
        var cli = clearInterval(window.yxyxyx_kam_intervalId);
        console.log(`清理保活循环任务: ${window.yxyxyx_kam_intervalId}`)
    }
    // 初始化现在时间
    var now = new Date();
    var formattedTime = now.getFullYear() + '-' + (now.getMonth() + 1).toString().padStart(2, '0') + '-' + now.getDate().toString().padStart(2, '0') + ' ' + now.getHours().toString().padStart(2, '0') + ':' + now.getMinutes().toString().padStart(2, '0') + ':' + now.getSeconds().toString().padStart(2, '0');
    console.log("初始化保活时间: " + formattedTime);
    // 判断keep_alive_minutes是否为空或者大于120分钟
    if (keep_alive_minutes === "" || parseInt(keep_alive_minutes) > 120) {
        console.log("保活时间不合法, 设置为默认的15分钟");
        keep_alive_minutes = 15
    }
    // 开始保活
    console.log(`开始保活，保活时间:${keep_alive_minutes}分钟`);
    function ClickConnect() {
        console.log("Working"); 
        document.getElementById("yxyx_keepalive_298432423").click();
    }
    
    // 计算保活时间的毫秒数
    var keep_alive_ms = keep_alive_minutes * 60 * 1000;
    
    // 执行保活函数，并存储 setInterval 返回的 ID
    var intervalId = setInterval(ClickConnect, 1000 * 30);
    window.yxyxyx_kam_intervalId = intervalId;
    // 在保活时间到期后清除定时器
    setTimeout(function() {
        console.log(`保活时间到期，停止保活: ${new Date()}`);
        try{
            clearInterval(intervalId);
            document.getElementById("yxyx_keepalive_675675").click();
        }catch(e){}
    }, keep_alive_ms);
}
"""

    def keepalive_output():
        return f"保活成功: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

    def stop_keepalive():
        return f"保活时间到期，停止保活: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

if 1:  # 重启
    def reboot_sd():
        """
        @des: 如果sd是后台启动，则只重启sd，不重启云函数实例
        """
        if yx_debug:
            return "重启服务成功"
        else:
            # 重启服务
            if 1:
                # 判断有没有supervisor进程,有的话杀死launch.py, 会自动重启
                command = """ps aux | grep "supervisord" | grep -v grep | awk \'{print $2}\' | head -n 1"""
                try:
                    output = subprocess.check_output(command, shell=True)
                    print("命令输出：", output)  # 命令输出： b'183273\n'
                except subprocess.CalledProcessError as e:
                    print("命令执行错误:", e)
                if output: # 如果是supervisor启动的
                    # 杀死launch.py, supervisor会自动重启
                    command1 = """kill -9 $(ps aux | grep "launch.py" | grep -v grep | awk '{print $2}' | head -n 1)"""
                    kill_output = subprocess.check_output(command1, shell=True)
                    print(f"重启sd进程:", kill_output)
                    return f"重启成功: {output} {kill_output}"
                else: # 直接docker的最后卡住命令启动的
                    # python增长内存来实现重启
                    # memory = []
                    # while True:
                    #     memory.append(' ' * 1000000)
                    # return f"{output} 实例重启"
                    return f"无supervisor启动的sd，无法重启"
            

    def reboot_sd_instance():
        """
        @des: 重启云函数实例
        """
        memory = []
        while True:
            memory.append(' ' * 1000000)
        