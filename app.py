import streamlit as st
import time  # 用于模拟延时

st.set_page_config(page_title='lover')

valid_names = ['唐悦媛', '葛青怡', '张雨萌', '居仕琪', '杨万兴', '赵吕聪',
               '刘莘', '周诣扬', '李瑞', '许志奥', '谷雨凡', '王其兰',
               '陈海军', '陈雯静', '程之璇', '徐葛薇蓉', '邓雯欣']

if 'page' not in st.session_state:
    st.session_state.page = 'main'

if st.session_state.page == 'main':
    st.title('姓名输入')
    name = st.text_input("请输入您的姓名")

    if st.button('开始'):
        with st.spinner('正在验证姓名...'):
            time.sleep(1)
            if name in valid_names:
                st.session_state.page = 'holiday'
            else:
                st.warning("姓名不在允许的列表中，请输入有效的姓名")

elif st.session_state.page == 'holiday':
    st.markdown("<h1 style='text-align: center;'>中秋快乐!!!</h1>", unsafe_allow_html=True)

    if st.button('返回首页', key='return_button', help='点击返回首页'):
        st.session_state.page = 'main'

