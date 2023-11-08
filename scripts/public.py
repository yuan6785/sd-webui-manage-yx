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