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
        if 1: # 保活:  会导致前端页面报错 Uncaught (in promise) TypeError: Cannot read ，但不影响啥
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
                html_not_error = gr.HTML("""""")
            greet_btn1 = gr.Button("更新保活时间", elem_id='yxyx_keepalive_12deqe')
            greet_btn1.click(fn=None, inputs=[
                            text_input1], outputs=[html_not_error], _js=get_window_url_params, api_name="greet1fds312")
            # demo加载的时候执行js函数
            depth_lib_1.load(fn=None, inputs=[text_input1],
                    outputs=[html_not_error],  _js=get_window_url_params)
    return [(depth_lib_1, "server manage", "depth_lib_1")]  # 界面上的选项
