import streamlit as st
import time  # 用于模拟进度增加的时间延迟

# 页面导航函数
def navigate_to_outline():
    with st.spinner('正在生成大纲...'):
        # 创建一个进度条的占位符
        progress_placeholder = st.empty()
        progress_bar = progress_placeholder.progress(0)


        # 模拟一个耗时的操作，例如生成大纲
        for i in range(100):
            # 更新进度条
            progress_bar.progress(i + 1)
            time.sleep(0.1)  # 模拟工作进程
        success_placeholder = st.empty()
        success_placeholder.success('完成 ✔️')
        # 进度完成后清除进度条
        progress_placeholder.empty()
        # time.sleep(5)
        success_placeholder.empty()

        # 假设这里是生成大纲的结果
        st.session_state.outline = f"{st.session_state.title_input} 的大纲内容示例"
    st.session_state.page = 'outline'  # 更新页面状态为大纲编辑页面

def back_to_input():
    st.session_state.page = 'input'  # 更新页面状态为输入页面

# 初始化会话状态变量
if 'title_input' not in st.session_state:
    st.session_state['title_input'] = ''
if 'outline' not in st.session_state:
    st.session_state['outline'] = ''
if 'page' not in st.session_state:
    st.session_state['page'] = 'input'

# 页面布局
if st.session_state.page == 'input':
    st.title('文章写作助手')
    title_input = st.text_input('请输入文章的标题', key='title_input')
    if st.button('确认', on_click=navigate_to_outline):
        # 按钮动作已经通过on_click指定，这里不需要额外的代码
        pass

elif st.session_state.page == 'outline':
    st.title('编辑大纲')
    edited_outline = st.text_area("编辑大纲内容", value=st.session_state.outline, height=250, key='edited_outline')
    st.session_state.outline = edited_outline  # 更新大纲内容
    if st.button('返回修改标题', on_click=back_to_input):
        pass
