import urllib.request
from bs4 import BeautifulSoup

# daum 야구

url = "https://v.daum.net/v/20221209035604569"
res = urllib.request.urlopen(url)

soup=BeautifulSoup(res,'html.parser')
title=soup.find('h3').string
# emotion=soup.find("alex_action_emotion").text


print(title)
print('-'*50)
for p in soup.select('p'):
    print(p.text)
# print(emotion)
