import requests
from bs4 import BeautifulSoup
from googlesearch import search

links=[]
query='Who was the Prime Minister of India when General Insurance was nationalised'
url='https://www.google.com/search?q='+query
# url='https://www.google.com/search?q=What+combination+of+three+letters+precede+web+site+addresses&oq=What+combination+of+three+letters+precede+web+site+addresses&aqs=chrome..69i57.967j0j1&sourceid=chrome&ie=UTF-8'
# Single google search
r=requests.get(url)
content=BeautifulSoup(r.text,'html.parser')
# print(content) Ap5OSd
text=content.find_all("div",class_="BNeawe")
test=''
for t in text:
    test+='\n'+t.text
print(test)
for j in search(query, tld="co.in", num=3, stop=3, pause=0):
    print(j)
    r1=requests.get(j)
    content1 = BeautifulSoup(r1.text, 'html.parser')
    text1 = content1.find("body")
    text1=text1.text
    test += '\n' + text1
    print("--------------------------------------------------------")
    print(test)