import requests
import time
import os
from bs4 import BeautifulSoup
from os import path


def web_News_scraping(file_path,Date,headers,Class_media,Class_time,state):
    with open(file_path, 'r' ,encoding="utf-8") as file:
      save =file.readlines()
    
    #整合網址迴圈
    a ='https://www.google.com.tw/search?q='
    b = '&tbm=nws'

    if state==0:
      #檢查是否存在
      if os.path.isdir('D:/daywork/look/'+ Date +'/'+Date+'新聞'):
          print('新聞已經儲存完畢')
          return
    if state==1:
      #檢查是否存在
      if os.path.isdir('D:/daywork/observation/News/'+Date+'新聞'):
          print('新聞已經儲存完畢')
          return

    #爬取新聞
    #新增資料夾
    if state==0:
      os.makedirs('D:/daywork/look/'+ Date +'/'+Date+'新聞')
    if state==1:
      os.makedirs('D:/daywork/observation/News/'+Date+'新聞')
    print('爬蟲開始')
    for i in range(len(save)):
      print('剩餘'+str(len(save)-i)+'檔股票')
      times=0
      c=save[i]
      c  = ' '.join(c.split())

      #刪除*
      if "*" in c:
          c=c.replace("*","")

      url = a+c+b
      res = requests.get(url, headers=headers) 
      time.sleep(2)
      res.encoding = 'utf-8'
      soup = BeautifulSoup(res.text,"html.parser") 

      #過濾奇摩

      span_tagsYahoo =soup.find_all("div", class_= [Class_media[0], Class_media[1]])
      
      for span_tag in span_tagsYahoo:
        if "奇摩" not in span_tag.span.string:
          #過濾時間
          span_tagsTime =soup.find_all("div", class_= [Class_time[0], Class_time[1]])
          aa=span_tagsTime[times].span.string

          if state==0:
            with open('D:/daywork/look/'+ Date +'/'+Date+'新聞/' + c +'.txt',"a",encoding="utf-8") as file:
             file.write(str(aa))
          
          if state==1:
            with open('D:/daywork/observation/News/'+Date+'新聞/' + c +'.txt',"a",encoding="utf-8") as file:
             file.write(str(aa))

        else:
          if state==0:
            with open('D:/daywork/look/'+ Date +'/'+Date+'新聞/' + c +'.txt',"a",encoding="utf-8") as file:
             file.write("0")
          
          if state==1:
            with open('D:/daywork/observation/News/'+Date+'新聞/' + c +'.txt',"a",encoding="utf-8") as file:
             file.write("0")

        times=times+1
      print(c+'新聞完成') 
    