"""
pyenv activate py3.11_virtualenv_test
"""
import os
import io
import json
import gradio as gr

yx_debug = True

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


def on_ui_tabs():
    with gr.Blocks(analytics_enabled=False) as depth_lib_1:
        gr.Markdown(
            """
        # Hello World!
        Start typing below to see the output.
        """)
        inp = gr.Textbox(placeholder="What is your name?")
        out = gr.Textbox()
        # inp.change(welcome, inp, out)
        # 创建按钮
        btn = gr.Button(value="提交")
        # 绑定按钮事件
        btn.click(welcome, inputs=[inp], outputs=[out])
        # 用于显示日志的html框
        gr.HTML("fsdafsdafsdafasf<br/>fdsfdsf<br/>哈哈哈佛")

    return [(depth_lib_1, "Yx Test", "depth_lib_1")]  # 界面上的选项


if not yx_debug:
    script_callbacks.on_ui_tabs(on_ui_tabs)
else:
    demo = on_ui_tabs()
    demo[0][0].launch()
