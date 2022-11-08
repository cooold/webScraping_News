import re
import os
import pandas as pd
import datetime

#read web data
def get_headers_save():
    with open('data_web/headers.txt', 'r' ,encoding="utf-8") as file:
      headers_save =file.read()
    print('讀取Header')
    return headers_save
def get_Class_time():
    with open('data_web/時間Class.txt', 'r' ,encoding="utf-8") as file:
      Class_time=file.read()
      Class_time=Class_time.split()
    print('讀取時間Class')
    return Class_time
def get_Class_media():
    with open('data_web/媒體Class.txt', 'r' ,encoding="utf-8") as file:
      Class_media =file.read()
      Class_media=Class_media.split()
    print('讀取媒體Class')
    return Class_media
def get_Class_title():
    with open('data_web/標題Class.txt', 'r' ,encoding="utf-8") as file:
      Class_title =file.read()
      Class_title='div.'+Class_title
    print('讀取標題Class')
    return Class_title
def get_Class_text():
    with open('data_web/內容Class.txt', 'r' ,encoding="utf-8") as file:
      Class_text =file.read()
      Class_text='div.'+Class_text
    print('讀取內容Class')
    return Class_text

#要得url
def get_url():
    with open('data_web/要得網址.txt', 'r' ,encoding="utf-8") as file:
      want_URL =file.readline()
    print('讀取網址')
    return want_URL

def get_InvestmentTrust_url1():
    with open('data_web/投信第一日上市.txt', 'r' ,encoding="utf-8") as file:
      want_URL =file.readline()
    print('讀取投信1')
    return want_URL

def get_InvestmentTrust_url2():
    with open('data_web/投信第一日上櫃.txt', 'r' ,encoding="utf-8") as file:
      want_URL =file.readline()
    print('讀取投信2')
    return want_URL

def get_historicalHigh_url():
    with open('data_web/歷史新高.txt', 'r' ,encoding="utf-8") as file:
      want_URL =file.readline()
    print('讀取歷史新高')
    return want_URL
#整理生成txt
def CVS_to_text(Date):
    #開啟 讀取 檔案
    with open('D:/daywork/StockList.csv', 'r' ,encoding="utf-8") as file:
        save_csv =file.readlines()
    #新增資料夾
    if os.path.isdir('D:/daywork/look/'+ Date ):
        print(Date+'資料夾已經存在')
    else:
      os.makedirs('D:/daywork/look/'+ Date )
      print(Date+'資料夾建立成功')
    
    #CSV轉TEXT
    for i in range (len(save_csv)):
      res=save_csv[i].split(',')
      #號碼
      number=res[0][2:6]
      #股票名稱
      a='"'
      name=re.sub(a, '', str(res[1]))
      if i!=0 and i<len(save_csv)-1:
        with open('D:/daywork/look/'+ Date+'/'+Date+'.txt',"a",encoding="utf-8") as file:
          file.write(number+' '+name+'\n')
      #最後不換行
      if i!=0 and i==len(save_csv)-1:
        with open('D:/daywork/look/'+ Date+'/'+Date+'.txt',"a",encoding="utf-8") as file:
          file.write(number+' '+name)
    print(Date+'txt檔案建立成功')

def show_todayNews(Date):

  print('顯示今日新聞')
  with open('D:/daywork/look/'+Date+'/'+'0小時NEW新聞個股.txt', 'r' ,encoding="utf-8") as file:
      show1=file.readlines()
      for i in range(len(show1)):
        print(show1[i])
  print('顯示觀察新聞')
  with open('D:/daywork/observation/'+'0小時NEW新聞個股.txt', 'r' ,encoding="utf-8") as file:
      show2=file.readlines()
      for i in range(len(show2)):
        print(show2[i])

def isNotHoliday(Date):
  currentDateTime = datetime.datetime.now()
  year = currentDateTime.date().strftime("%Y")
  setDate=year+'-'+Date[0:2]+'-'+Date[2:]
  temp = pd.Timestamp(setDate)
  DayName=temp.day_name()
  print("今天是"+DayName)
  if DayName=='Saturday' or DayName=='Sunday':
    return False
  else:
    return True
