import streamlit as st
import streamlit.components.v1 as stc
import makelist_app, trans_anker_app, trans_pc_app, opt_table_app

st.set_page_config(
    page_title="HarumakeTools",
    layout="wide",
    initial_sidebar_state="expanded"
)

# stc.html("""
#         <html lang="ja">
#         <head>
#             <meta charset="UTF-8">
#             <meta http-equiv="X-UA-Compatible" content="IE=edge">
#             <meta name="viewport" content="width=device-width, initial-scale=1.0">
#             <title>HarumakeTools</title>
#         </head>
#         """,)

footer="""<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: white;
color: black;
text-align: center;
}
</style>
<div class="footer">
<p><a style='display: block; text-align: center;' href="https://ma-ke-univ.com/" target="_blank">Webマーケ大学</a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)

PAGES = {
    "リスト作成アプリ": makelist_app,
    "アンカー・英語翻訳アプリ": trans_anker_app,
    '画像・英語翻訳アプリ': trans_pc_app,
    '表最適化アプリ':opt_table_app
}
st.title('HarumakeTools')
st.sidebar.title('アプリケーションの選択！')
link = '[使い方はこちら！](https://ma-ke-univ.com/harumaketools.html)'
st.markdown(link, unsafe_allow_html=True)
selection = st.sidebar.radio("使いたいアプリを選択してね！", list(PAGES.keys()))
page = PAGES[selection]
page.app()
