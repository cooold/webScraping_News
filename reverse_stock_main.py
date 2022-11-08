import base_function,downloadCSV,Web_Scraping,analysis_news_time

#問日期
print('請輸入日期')
Date=input()

#讀取爬蟲需要資料
headers_save =base_function.get_headers_save()
Class_time=base_function.get_Class_time()
Class_media=base_function.get_Class_media()
Class_title=base_function.get_Class_title()
Class_text=base_function.get_Class_title()


#建立headers和網址
headers = {'user-agent': headers_save }
url=base_function.get_url()

historicalHigh_url=base_function.get_historicalHigh_url()
InvestmentTrust_url1=base_function.get_InvestmentTrust_url1()
InvestmentTrust_url2=base_function.get_InvestmentTrust_url2()

#假日不抓
Holiday=base_function.isNotHoliday(Date)
if Holiday:
    print('X今天不是假日,抓取投信和歷史新高X')
    #抓取投信第一日購買和歷史新高html
    downloadCSV.download_html(headers=headers,url=historicalHigh_url,state=0,Date=Date)
    downloadCSV.download_html(headers=headers,url=InvestmentTrust_url1,state=1,Date=Date)
    downloadCSV.download_html(headers=headers,url=InvestmentTrust_url2,state=2,Date=Date)
else:
    print('O今天是假日,跳過抓取投信和歷史新高O')

#抓取csv檔案
downloadCSV.download_csv(headers=headers,url=url)

#CSV轉text
base_function.CVS_to_text(Date)

#爬新聞

#每日新聞
dayNews_path='D:/daywork/look/'+ Date +'/' + Date +'.txt'
print('每日新聞開始')
Web_Scraping.web_News_scraping(file_path=dayNews_path,Date=Date,headers=headers,Class_media=Class_media,Class_time=Class_time,state=0)
print('每日新聞獲取完成')
print('---------------------------------------')
#觀察新聞
observation_path='D:/daywork/observation/observation.txt'
print('觀察新聞開始')
Web_Scraping.web_News_scraping(file_path=observation_path,Date=Date,headers=headers,Class_media=Class_media,Class_time=Class_time,state=1)
print('觀察新聞獲取完成')
print('---------------------------------------')
#分析新聞時間
#建立資料夾
analysis_news_time.new_folder_txt(Date=Date)
#每日新聞
print('分析每日新聞開始')
analysis_news_time.analysis_news(Date=Date,state=0)
print('分析每日新聞完成')
print('---------------------------------------')
#觀察新聞
print('分析觀察新聞開始')
analysis_news_time.analysis_news(Date=Date,state=1)
print('分析觀察新聞完成')
print('---------------------------------------')

base_function.show_todayNews(Date=Date)
aa=input()