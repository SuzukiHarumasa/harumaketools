import streamlit as st
from moduls import opt_table
from PIL import Image


def app():
        
    st.title('テーブル最適化アプリだよ！')

    piyotaso = Image.open('./static/piyotaso.png')
    piyotaso_odoroki = Image.open('./static/piyotaso_odoroki.png')
    image_chikin = Image.open('./static/corean_chikin.jpeg')
    txt = st.text_area('最適化したいテーブルのHTMLを入力してね！')
    col1, col2, col3 = st.columns(3)

    button = st.button('入力してクリック！')

    if not button:
        with col2:
            st.image(piyotaso,width=300)

    if button:
        if txt:
            res = opt_table(txt)
            if res:
                col1, col2= st.columns(2)
                with col1:
                    st.image(image_chikin,width=300)
                with col2:
                    st.image(piyotaso_odoroki,width=300)
                st.success('最適化完了！！！')
                st.code(res, language = 'html')

                