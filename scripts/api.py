"""
可以参考dreambooth和controlnet的api.py

/docs可以看到api调用方式
"""
from typing import Union

import numpy as np
from fastapi import FastAPI, Body
import copy
import pydantic
import sys

import gradio as gr

from modules.api.models import *
from modules.api import api

from scripts import external_code
from scripts.processor import *
import os
from fastapi.responses import HTMLResponse


def server_manage_yx_api(_: gr.Blocks, app: FastAPI):
    @app.get("/servermanageyx/version")
    async def version():
        return {"version": '1.0'}

    # 查看日志等等也可以写到这里面，不用写到fast_main.py里面
    @app.get("/servermanageyx/getlog", response_class=HTMLResponse)
    async def get_sd_log():
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


try:
    import modules.script_callbacks as script_callbacks

    script_callbacks.on_app_started(server_manage_yx_api)
except:
    pass
