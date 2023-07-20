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
from fastapi.responses import HTMLResponse, FileResponse
# 读取运行时的数据
from modules import script_callbacks, scripts, sd_hijack, shared


def server_manage_yx_api(_: gr.Blocks, app: FastAPI):
    @app.get("/servermanageyx/version")
    async def version():
        return {"version": '1.0'}
    
    @app.get("/servermanageyx/downloadlog")
    async def download_log():
        # 取文件sd.log的最后300行
        filepath = "./sd.log"
        # 判断文件是否存在
        if not os.path.exists(filepath):
            filepath = "/var/log/sdwebui/sd.log"
            if not os.path.exists(filepath):
                filepath = "/var/log/sdwebui.log"
                if not os.path.exists(filepath):
                    return "sd.log文件不存在"
        return FileResponse(filepath, filename=os.path.basename(filepath))

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
    
    @app.get("/servermanageyx/getsytlesruntime")
    async def get_sytles_runtime():
        result = {"styles": 'no data'}
        try:
            # 如果要删除styles.csv里面的内容，需要这样删除 del shared.prompt_styles.styles[name], 不可以直接删除csv的内容，无效的，需要删除运行时内存的内容
            result = shared.prompt_styles.styles 
        except:
            pass
        return result



try:
    import modules.script_callbacks as script_callbacks

    script_callbacks.on_app_started(server_manage_yx_api)
except:
    pass
