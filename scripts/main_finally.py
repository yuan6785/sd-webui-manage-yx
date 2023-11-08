"""
pyenv activate py3.11_virtualenv_test
"""
from scripts.public import *


def on_ui_tabs():
    with gr.Blocks(analytics_enabled=False) as depth_lib_1:
        if 1: # 调整其他服务的链接
            html1 = gr.HTML("""
            <font>----------------------------------------------------------------</font><br/>
            <a id="yxyxyx_viewlog_hreda111" href='https://sd.agones.playdayy.cn/psuperfaa/' target='_blank'>服务器管理页面(日志和重启)</a><br/>
            <font>----------------------------------------------------------------</font><br/>
            <a id="yxyxyx_viewlog_hreda111" href='https://minio-web.agones.playdayy.cn/minio_iframe_1/' target='_blank'>文件上传管理</a><br/>
            <font>----------------------------------------------------------------</font><br/>
            """)
    return [(depth_lib_1, "server manage", "depth_lib_1")]  # 界面上的选项
