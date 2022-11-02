import requests
import os
#from fake_useragent import UserAgent
from bs4 import BeautifulSoup
#ua = UserAgent()
#header = {'User-Agent':str(ua.chrome)}

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
url='//www.enteryourweb.com/read/name of manga preferebly/chapter-1'
r=requests.get(url,headers=headers)
rsponse_code=r.status_code
print(rsponse_code)

soup=BeautifulSoup(r.content,'html.parser')
filename=url.split('/')[-3].title().replace('-',' ')
#have to check your page to check what class name it uses 
lst=soup.find_all(class_="wp-manga-chapter-img")
#where to save your downloaded manga
path=''
if rsponse_code==200:
    # put path you want to save to
    if filename not in os.listdir(path):
        #make the folder to hold the chapters if not available
        os.mkdir(f'{path}/{filename}')
    for ur in lst:
        r=requests.get(ur['src'].strip(),headers=headers)
        print(r.status_code)
        #can choose where to save and name each picture downloaded
        with open(f'/{path}/{filename}/{filename.lower()}.jpg','wb') as f:
            f.write(r.content)
