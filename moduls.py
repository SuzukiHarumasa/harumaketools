from googletrans import Translator
from bs4 import BeautifulSoup
import re

def makelist(text: str, ty):
    lists = []
    for li in text.split('・')[1:]:
        li = '<li>'+li+'</li>'
        lists.append(li)
        
    strlist = ''.join(lists)
    
    if ty == '番号':
        strlist = '<ol>'+strlist+'</ol>'
    elif ty == '普通':
        strlist = '<ul>'+strlist+'</ul>'
        
    return strlist

class TranceAncker():

    def translate_ja(self, txt):
        tr = Translator()
        txt = ''.join(filter(str.isalnum, txt))
        txt = tr.translate(txt, src="ja", dest="en").text.lower().replace(' ', '_')
        return txt

    def trans_anker(self, list_html):
        soup = BeautifulSoup(list_html, 'html.parser')
        lists = soup.find_all('li')
        txt_list = []
        for lis in lists:
            txt = self.translate_ja(lis.text)
            
            txt_list.append(txt)

            
        return txt_list
    
    def trans_anker_list(self, list_html):
    
    
        soup = BeautifulSoup(list_html, 'html.parser')
        
        lists = soup.find_all('li')
        txt_list = []
        h3_list = []
        for lis in lists:
            txt = self.translate_ja(lis.text)
            
            #リスト作成
            li = '<li></li>'
            soup_li = BeautifulSoup(li, 'html.parser')
            tag = soup.new_tag('a', href='#'+txt)
            tag.string = lis.string
            soup_li.li.append(tag)
            txt_list.append(soup_li)
            
            #h3作成
            h3 = '<h3></h3>'
            soup_h3 = BeautifulSoup(h3, 'html.parser')
            tag_h3 = soup.new_tag('a', id=txt)
            
            soup_h3.h3.string= lis.string
            soup_h3.h3.append(tag_h3)
            
            h3_list.append(soup_h3)

        txt_list = "".join(map(str, txt_list))
        
            
        return txt_list,h3_list
    

def opt_table(html):
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find_all('table')
    tables = soup.find_all('table')

    for table in tables:
        del table['style']

    for table in tables:
        del table['border']

    for table in tables:
        del table['cellpadding']

    for table in tables:
        del table['cellspacing']
        
    for table in tables:
        del table['dir']

    for table in tables:
        table['class'] = "tb-responsive aligncenter"
        
    calgroups = soup.find_all('colgroup')

    for calgroup in calgroups:
        del calgroup['style']

    cols = soup.find_all('col')

    for col in cols:
        del col['width']
        del col['height']

    ths = soup.find_all('th')

    for th in ths:
        del th['style']

    trs  = soup.find_all('tr')

    for tr in trs:
        del tr['style']

    tds  = soup.find_all('td')

    for td in tds:
        del td['style']
        del td['data-sheets-value']
        spans = td.find_all('span')
        if spans:
            for span in spans:
                del span['style']
        
        
    return soup