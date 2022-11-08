import requests
import time
import os
from bs4 import BeautifulSoup
from os import path
import webbrowser   
import re

def download_csv(headers,url):
    #爬取資料
    res = requests.get(url, headers=headers) 
    res.encoding = 'utf-8'
    if res.status_code == 200:
       print("篩選網站成功回應")
    else:
        print("爬取失敗，伺服器沒有回應")
    #處理格式加入需要的東西
    with open('D:/daywork/TemporarilySave/dow.txt', 'r' ,encoding="utf-8") as file:
        save_dow =file.readlines()
    soup = BeautifulSoup(res.text,"html.parser")

    #刪除舊的
    if os.path.isfile('D:/daywork/TemporarilySave/save.html'):
        os.remove('D:/daywork/TemporarilySave/save.html')
        print("刪除舊的篩選save.html >> D:/daywork/TemporarilySave/save.html")

    #建立新的
    with open('D:/daywork/TemporarilySave/save.html',"a",encoding="utf-8") as file:
        for i in range (len(save_dow)):
            file.write(str(save_dow[i]))
        file.write(str(soup))
    print("save.html已更新")

    #註冊瀏覽器
    firefoxPath = "C:/Program Files/Mozilla Firefox/firefox.exe"
    webbrowser.register('firefox', None, webbrowser.BackgroundBrowser(firefoxPath))

    #刪除舊的
    if os.path.isfile('D:/daywork/StockList.csv'):
        print("刪除舊的篩選/StockList.csv >> D:/daywork/StockList.csv")
        os.remove('D:/daywork/StockList.csv')
    
    #開啟下載
    webbrowser.get('firefox').open('file:///D:/daywork/TemporarilySave/save.html')
    time.sleep(8)

def download_html(headers,url,state,Date):
    #爬取資料
    res = requests.get(url, headers=headers) 
    res.encoding = 'utf-8'
    if res.status_code == 200:
       print("篩選網站成功回應")
    else:
        print("爬取失敗，伺服器沒有回應")
    soup = BeautifulSoup(res.text,"html.parser")
    #建立html
    if state==0:
        with open('D:/daywork/historicalHigh/'+Date+'歷史新高.html',"a",encoding="utf-8") as file:
          file.write(str(soup))
    if state==1:
        with open('D:/daywork/InvestmentTrust/'+Date+'投信上市.html',"a",encoding="utf-8") as file:
          file.write(str(soup))
    if state==2:
        with open('D:/daywork/InvestmentTrust/'+Date+'投信上櫃.html',"a",encoding="utf-8") as file:
          file.write(str(soup))
    time.sleep(5)
    