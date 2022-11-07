import streamlit as st
from PIL import Image
import numpy as np
import os
from moduls import TranceAncker



def app():
    translater = TranceAncker()
    st.markdown('# 画像の名前を英語に変換するアプリだよ！')
    text_ja = st.text_input('画像にあった語句を入れてね！(日本語)')
    file = st.file_uploader('画像をアップロードしてください.', type=['jpg', 'jpeg', 'png'])
    if file:
        if not text_ja:
            st.error('画像にあった語句を入れてください！')
        else:
            extension = file.name.split('.')[-1]
            file.name = translater.translate_ja(text_ja)
            file.name = file.name+'.'+extension
            st.markdown(f'{file.name} をアップロードしました.')
            
            
            # 保存した画像を表示
            img = Image.open(file)
            st.image(img)
        
        # ダウンロード
        st.download_button(
            label = 'ダウンロード',
            data = file,
            file_name = file.name,
            
        )
