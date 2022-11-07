import streamlit as st
from moduls import makelist

def app():

    st.markdown('# リスト作成ツール')

    text = st.text_area(
    'リストにしたい文字列を入れてください！',
    placeholder = '''
    ・リスト1つ目
    ・リスト2つ目
    ・リスト3つ目
    ''')
    ty = st.selectbox("リストの形式を選んでね！", ('普通', '番号'))


    if st.button('入力したらクリック！'):
        
        if ty and text:
            strlist = makelist(text, ty)
                
            if strlist:
                    st.code(strlist)
        
        else:
            st.error("テキストかタイプが入っていません！")