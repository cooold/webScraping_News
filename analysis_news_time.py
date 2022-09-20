import os

def new_folder_txt(Date):

    #每日新聞txt
    resText0= open('D:/daywork/look/'+ Date +'/NEW新聞個股.txt',"a",encoding="utf-8")
    resText1= open('D:/daywork/look/'+ Date +'/0小時NEW新聞個股.txt',"a",encoding="utf-8")
    resText2= open('D:/daywork/look/'+ Date +'/1天NEW新聞個股.txt',"a",encoding="utf-8")
    resText3= open('D:/daywork/look/'+ Date +'/2週NEW新聞個股.txt',"a",encoding="utf-8")
    resText4= open('D:/daywork/look/'+ Date +'/3月NEW新聞個股.txt',"a",encoding="utf-8")
    resText5= open('D:/daywork/look/'+ Date +'/4無NEW新聞個股.txt',"a",encoding="utf-8")
    
    resText0.close()
    resText1.close()
    resText2.close()
    resText3.close()
    resText4.close()
    resText5.close()

    #觀察新聞txt
    if os.path.isfile('D:/daywork/observation/NEW新聞個股.txt'):
      #每日刪除
      os.remove('D:/daywork/observation/NEW新聞個股.txt')
      os.remove('D:/daywork/observation/0小時NEW新聞個股.txt')
      os.remove('D:/daywork/observation/1天NEW新聞個股.txt')
      os.remove('D:/daywork/observation/2週NEW新聞個股.txt')
      os.remove('D:/daywork/observation/3月NEW新聞個股.txt')
      os.remove('D:/daywork/observation/4無NEW新聞個股.txt')
    #建立txt
    resText00= open('D:/daywork/observation/NEW新聞個股.txt',"a",encoding="utf-8")
    resText01= open('D:/daywork/observation/0小時NEW新聞個股.txt',"a",encoding="utf-8")
    resText02= open('D:/daywork/observation/1天NEW新聞個股.txt',"a",encoding="utf-8")
    resText03= open('D:/daywork/observation/2週NEW新聞個股.txt',"a",encoding="utf-8")
    resText04= open('D:/daywork/observation/3月NEW新聞個股.txt',"a",encoding="utf-8")
    resText05= open('D:/daywork/observation/4無NEW新聞個股.txt',"a",encoding="utf-8")

    resText00.close()
    resText01.close()
    resText02.close()
    resText03.close()
    resText04.close()
    resText05.close()



def analysis_news(Date,state):
    #每日
    if state==0:
        with open('D:/daywork/look/'+ Date +'/' + Date +'.txt', 'r' ,encoding="utf-8") as file:
            save =file.readlines()
        print ('每日新聞個股有'+str(len(save)))
    #觀察
    if state==1:
        with open('D:/daywork/observation/observation.txt', 'r' ,encoding="utf-8") as file:
            save =file.readlines()
        print ('觀察新聞個股有'+str(len(save)))

    for i in range(len(save)):
        findname=' '.join(save[i].split())

         #刪除*
        if "*" in findname:
          findname=findname.replace("*","")

        if state==0:
          with open('D:/daywork/look/'+ Date +'/' + Date +'新聞/'+findname+'.txt', 'r' ,encoding="utf-8") as file:
            context =file.read()
        if state==1:
          with open('D:/daywork/observation/News/'+Date+'新聞/'+findname+'.txt', 'r' ,encoding="utf-8") as file:
            context =file.read()
        
        #計算時間次數
        countMinutes=context.count('分鐘前')
        countHours=context.count('小時前')
        countDays=context.count('天前')
        countWeeks=context.count('週前')
        countMonth=context.count('個月前')
        allTimes=str(countMinutes)+str(countHours)+str(countDays)+str(countWeeks)+str(countMonth)

        if state==0:
          with open('D:/daywork/look/'+ Date +'/NEW新聞個股.txt',"a",encoding="utf-8") as file:
            file.write(findname+','+str(allTimes)+'\n')

          if countMinutes>=1 or countHours>=1:
            with open('D:/daywork/look/'+ Date +'/0小時NEW新聞個股.txt',"a",encoding="utf-8") as file:
              file.write(findname+','+str(allTimes)+'\n')
          elif countDays>=1:
            with open('D:/daywork/look/'+ Date +'/1天NEW新聞個股.txt',"a",encoding="utf-8") as file:
                file.write(findname+','+str(allTimes)+'\n')
          elif countWeeks>=1:
            with open('D:/daywork/look/'+ Date +'/2週NEW新聞個股.txt',"a",encoding="utf-8") as file:
                file.write(findname+','+str(allTimes)+'\n')
          elif countMonth>=1:
            with open('D:/daywork/look/'+ Date +'/3月NEW新聞個股.txt',"a",encoding="utf-8") as file:
                file.write(findname+','+str(allTimes)+'\n')
          else:
            with open('D:/daywork/look/'+ Date +'/4無NEW新聞個股.txt',"a",encoding="utf-8") as file:
                file.write(findname+','+str(allTimes)+'\n')
          


        if state==1:
          with open('D:/daywork/observation/NEW新聞個股.txt',"a",encoding="utf-8") as file:
            file.write(findname+','+str(allTimes)+'\n')

          if countMinutes>=1 or countHours>=1:
            with open('D:/daywork/observation/0小時NEW新聞個股.txt',"a",encoding="utf-8") as file:
              file.write(findname+','+str(allTimes)+'\n')
          elif countDays>=1:
            with open('D:/daywork/observation/1天NEW新聞個股.txt',"a",encoding="utf-8")as file:
                file.write(findname+','+str(allTimes)+'\n')
          elif countWeeks>=1:
            with open('D:/daywork/observation/2週NEW新聞個股.txt',"a",encoding="utf-8") as file:
                file.write(findname+','+str(allTimes)+'\n')
          elif countMonth>=1:
            with open('D:/daywork/observation/3月NEW新聞個股.txt',"a",encoding="utf-8") as file:
                file.write(findname+','+str(allTimes)+'\n')
          else:
            with open('D:/daywork/observation/4無NEW新聞個股.txt',"a",encoding="utf-8") as file:
                file.write(findname+','+str(allTimes)+'\n')
    


        


