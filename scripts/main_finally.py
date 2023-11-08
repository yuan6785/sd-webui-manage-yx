"""
pyenv activate py3.11_virtualenv_test
"""
from scripts.public import *
import requests
import re

public_ip = None

def get_public_ip():
    global public_ip
    if public_ip is None:
        for i in range(5):
            try:
                res = requests.get('http://100.100.100.200/latest/meta-data/eipv4', timeout=(5, 5))
                if res.status_code != 200:
                    raise Exception('status_code != 200')
                public_ip = res.text
                # 正则表达式判断是否是ip
                if re.match(r'^\d+\.\d+\.\d+\.\d+$', public_ip) is None:
                    raise Exception('not ip')
                break
            except:
                time.sleep(5)
    return public_ip

def on_ui_tabs():
    with gr.Blocks(analytics_enabled=False) as depth_lib_1:
        if 1: # 调整其他服务的链接
            real_public_ip = get_public_ip()
            if real_public_ip is None:
                html1 = gr.HTML("""
                <font>---------------------------获取本机公共ip失败-------------------------------</font><br/>"""
                )
            else:
                html1 = gr.HTML(f"""
                <font>----------------------------------------------------------------</font><br/>
                <a id="yxyxyx_viewlog_hreda111" href='http://{real_public_ip}:9001/' target='_blank'>服务器管理页面(日志和重启)</a><br/>
                <font>----------------------------------------------------------------</font><br/>
                <a id="yxyxyx_viewlog_hreda111" href='http://{real_public_ip}:9003' target='_blank'>文件上传管理</a>--><font>(用户名:ecsuser &nbsp;&nbsp; 密码:ecsuserqwe)</font><br/>
                <font>----------------------------------------------------------------</font><br/>
                """)
    return [(depth_lib_1, "server manage", "depth_lib_1")]  # 界面上的选项
