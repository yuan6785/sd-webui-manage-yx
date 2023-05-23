import os
import io
import json
import gradio as gr

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


    return [(depth_lib_1, "Yx Test", "depth_lib_1")]  # 界面上的选项





script_callbacks.on_ui_tabs(on_ui_tabs)
