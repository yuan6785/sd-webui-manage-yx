"""
pyenv activate py3.11_virtualenv_test
"""
import os
import io
import json
import gradio as gr
# 判断mac还是linux系统
import platform
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
                return "sd.log文件不存在"
        count = 300
        with open(filepath, "r") as f:
            lines = f.readlines()
            lines = lines[-count:]
            lines = "<br/>".join(lines)
            return lines

def reboot_sd():
    if yx_debug:
        return "重启服务成功" 
    else:
        # 重启服务
        res = os.system("""kill -9 $(ps aux | grep "launch.py" | grep -v grep | awk '{print $2}' | head -n 1)""")
        print("yx kill----", res)
        return "重启服务成功" 


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
        # 用于显示日志的html框
        btn = gr.Button(value="查看日志")
        html = gr.HTML("")
        # 绑定按钮事件
        btn.click(get_sd_log, inputs=[], outputs=[html])
        # # 重启服务按钮
        # btn_reboot = gr.Button(value="重启服务")
        # # 绑定按钮事件
        # btn_reboot.click(reboot_sd, inputs=[], outputs=[])


    return [(depth_lib_1, "Yx Test", "depth_lib_1")]  # 界面上的选项


if not yx_debug:
    script_callbacks.on_ui_tabs(on_ui_tabs)
else:
    demo = on_ui_tabs()
    demo[0][0].launch()
