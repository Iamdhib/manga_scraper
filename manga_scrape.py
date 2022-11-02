from fileinput import filename
import requests
import os
#from fake_useragent import UserAgent
from bs4 import BeautifulSoup
#ua = UserAgent()
#header = {'User-Agent':str(ua.chrome)}

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
url='https://aquamanga.com/read/archmage-transcending-through-regression/chapter-2/'
r=requests.get(url,headers=headers)
rsponse_code=r.status_code
print(rsponse_code)

soup=BeautifulSoup(r.content,'html.parser')
filename=url.split('/')[-3].title().replace('-',' ')
lst=soup.find_all(class_="wp-manga-chapter-img")
if rsponse_code==200:
    if filename not in os.listdir('/home/iamdhib/Pictures/MMM'):
        os.mkdir(f'/home/iamdhib/Pictures/MMM/{filename}')
    for ur in lst:
        r=requests.get(ur['src'].strip(),headers=headers)
        print(r.status_code)
        with open(f'/home/iamdhib/Pictures/MMM/{filename}/{filename.lower()}.jpg','wb') as f:
            f.write(r.content)
    pass 