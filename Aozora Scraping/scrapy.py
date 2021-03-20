import urllib.request
from bs4 import BeautifulSoup

text = []

#対象サイトのURL
url = 'https://www.aozora.gr.jp/cards/000081/files/456_15050.html'
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html,'html.parser')

#classではなくclass_とすることに注意する
ginga =  soup.findAll('div' , class_= 'main_text')

for i in ginga:
#テキストだけ取り出し追加していく
    text.append(i.text)

#ginga.txtという名前でテキストファイルとして保存する
file = open('ginga.txt','w',encoding='utf-8')
file.writelines(text)
file.close()
