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
    def get_sd_log():
        if yx_debug:
            return "test log"
        else:
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
                return lines

if 1:  # 保活
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
        @des: only ecs, not aliyun-fc
        """
        if yx_debug:
            return "重启服务成功"
        else:
            # 重启服务
            if 0:
                res = os.system(
                    """kill -9 $(ps aux | grep "launch.py" | grep -v grep | awk '{print $2}' | head -n 1)""")
                print("yx kill----", res)
                time.sleep(5)
                return f"重启服务成功,{res}"
            if 1:
                # python增长内存来实现重启
                memory = []
                while True:
                    memory.append(' ' * 1000000)


def on_ui_tabs():
    with gr.Blocks(analytics_enabled=False) as depth_lib_1:
        # if 0: # 测试
        #     gr.Markdown(
        #         """
        #     # Hello World!
        #     Start typing below to see the output.
        #     """)
        #     inp = gr.Textbox(placeholder="What is your name?")
        #     out = gr.Textbox()
        #     # inp.change(welcome, inp, out)
        #     # 创建按钮
        #     btn = gr.Button(value="提交")
        #     # 绑定按钮事件
        #     btn.click(welcome, inputs=[inp], outputs=[out])
        if 1:
            # 用于显示日志的html框
            btn = gr.Button(value="查看日志")
            html = gr.HTML("")
            # 绑定按钮事件
            btn.click(get_sd_log, inputs=[], outputs=[html])
        if 0: # 保活:  会导致前端页面报错 Uncaught (in promise) TypeError: Cannot read ，但不影响啥
            # input
            text_input1 = gr.Textbox(lines=1, label="保活时间(分钟),默认15分钟,最大不超过120分钟")
            text_output1 = gr.Textbox(lines=1, label="保活输出")
            with gr.Row(visible=False):
                greet_btn = gr.Button("隐藏保活操作按钮", elem_id='yxyx_keepalive_298432423')
                greet_btn.click(fn=keepalive_output, inputs=None, outputs=[
                                text_output1], api_name="greet123af")
                stop_btn = gr.Button("停止保活", elem_id='yxyx_keepalive_675675')
                stop_btn.click(fn=stop_keepalive, inputs=None, outputs=[
                                text_output1], api_name="3123123fdsfds")
            greet_btn1 = gr.Button("更新保活时间", elem_id='yxyx_keepalive_12deqe')
            greet_btn1.click(fn=None, inputs=[
                            text_input1], outputs=None, _js=get_window_url_params, api_name="greet1fds312")
            # demo加载的时候执行js函数
            depth_lib_1.load(fn=None, inputs=[text_input1],
                    outputs=None,  _js=get_window_url_params)
        if 0:
            # 重启服务按钮
            btn_reboot = gr.Button(value="重启服务")
            # 重启日志输出
            html_reboot = gr.HTML("")
            # 绑定按钮事件
            btn_reboot.click(reboot_sd, inputs=[], outputs=[html_reboot])

    return [(depth_lib_1, "server manage", "depth_lib_1")]  # 界面上的选项


if not yx_debug:
    script_callbacks.on_ui_tabs(on_ui_tabs)
else:
    demo = on_ui_tabs()
    demo[0][0].launch()
