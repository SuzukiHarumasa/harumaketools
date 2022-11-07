import streamlit as st
from moduls import TranceAncker

def app():
    
    translator = TranceAncker()

    st.markdown('# アンカータグ・英語翻訳ツール！')

    text = st.text_area(
    '翻訳したいリストのhtmlコードを入れてね！',
    placeholder = '''
    <li>リスト1つ目</li>
    <li>リスト2つ目</li>
    <li>リスト3つ目</li>
    ''')


    if st.button('入力したらクリック！'):
        
        if text:
            strlist = translator.trans_anker(text)
            stranker, h3s = translator.trans_anker_list(text)
                
            if strlist:
                for li in strlist:
                    st.code(li)
                st.write('## h2以下のリスト用だよ！（HTML）')
                st.code(stranker)
                st.write('## h3用だよ！（HTML）')
                for h3 in h3s:
                    st.code(h3)
        
        else:
            st.error("テキストが入っていません！")