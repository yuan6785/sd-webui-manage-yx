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
import arrow
if platform.system() == 'Darwin':
    yx_debug = True
elif platform.system() == 'Linux':
    yx_debug = False

if not yx_debug:
    from modules import script_callbacks, scripts, sd_hijack, shared
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
        # 利用arrow输出北京时间
        rs = arrow.now().to('Asia/Shanghai').format('YYYY-MM-DD HH:mm:ss')
        return f"保活成功: {rs}"
        # return f"保活成功: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

    def stop_keepalive():
        rs = arrow.now().to('Asia/Shanghai').format('YYYY-MM-DD HH:mm:ss')
        return f"保活时间到期，停止保活: {rs}"
        # return f"保活时间到期，停止保活: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
