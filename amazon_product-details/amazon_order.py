import requests,time,smtplib
from bs4 import BeautifulSoup
from notify_run import Notify
from datetime import datetime
import pandas as pd
url='https://www.amazon.in/s?k=trimmer&i=stripbooks&ref=nb_sb_noss_1'
#url=input()
dp=1000
URL=url
pnmsg="Below Rs. '+str(dp)+' you can get your Philips Trimmer."
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0;Win64;x64) AppeWebKit/537.36(KHTML, like Gecko) Crome/76.0.3809.132 Safari/537.36"}
def check_price():
    thislist=[]
    list1=[]
    list2=[]
    page=requests.get(URL,headers=headers)
    soup=BeautifulSoup(page.content,'html.parser')
    price=soup.find('span',class_='a-price-whole')
    #print(price)

    w = soup.find_all('span',class_='a-price-whole')
    hlink=soup.find_all("a",class_='a-link-normal a-text-normal')
    length=len(w)
    for win in range(length):
        t=w[win].text
        #print(t)
        #print(t.replace(',',''))
        #print(int(t.replace(',','')))
    title=soup.find_all('span',class_="a-size-medium a-color-base a-text-normal")
    for i in range(len(w)):
        t=w[i].text
        print(str("Price: "+ w[i].text+";"+" Title: "+title[i].text))
        if(int(float((t.replace(',',''))))==0):
            pass
        elif(int(float((t.replace(',',''))))<1000):
            #thislist.append(str(w[i].text+","+title[i].text+","+hlink[i].text))
            list1.append(str(w[i].text))
            list2.append(str(title[i].text))


   # print(thislist)
    df=pd.DataFrame(list1,list2,columns=["price"])
    print(df)
    #   print(paragraph.string)
     #  print(str(paragraph.text))

check_price()