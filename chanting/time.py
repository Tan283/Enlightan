
import requests
import time
from requests_html import HTMLSession
from datetime import date
import calendar

def scraping():
    session = HTMLSession()
    res = session.get("https://www.timeanddate.com/moon/phases/")

    sel = 'body > div.main-content-div > main > article > section.fixed > div.row.dashb.pdflexi > div > table > tbody'
    table = res.html.find(sel, first=False)
    j = ''
    for i in table:
        j+=(i.text.replace("\n"," "))
        l = j.split(" ")

    months = ['มกราคม','กุมภาพันธ์','มีนาคม','เมษายน','พฤษภาคม','มิถุนายน','กรกฎาคม','สิงหาคม','กันยายน','ตุลาคม','พฤศจิกายน','ธันวาคม']
    emp = []
    for i in range(len(l)):
        j = i + 1 
        if j < len(l):
            if(l[j] in months):
                word = l[i]+"/"+str(month_converter(l[j]))
                emp.append(word)    
    return emp

def month_converter(month):
    months = ['มกราคม','กุมภาพันธ์','มีนาคม','เมษายน','พฤษภาคม','มิถุนายน','กรกฎาคม','สิงหาคม','กันยายน','ตุลาคม','พฤศจิกายน','ธันวาคม']
    if(months.index(month) + 1 < 10):
        return "0"+str(months.index(month) + 1)
    else:
        return months.index(month) + 1


# def monk_day():
#     today = date.today()
#     day = today.strftime("%d/%m/%Y")
#     period = scraping()
#     return day[:len(day)-5] in period

def monk_day():
    today = date.today()
    dmy = today.strftime("%d/%m/%Y")
    period = scraping()
    day,month,year = dmy.split('/')
    day = int(day)
    month = int(month)
    year = int(month)
    distance = -1
    for i in range (0,len(period)):
        pd,pm = period[i].split("/")
        pd = int(pd)
        pm = int(pm)
    
        if(pm == month):
            if(day <= pd):
                distance = pd-day
                break
        if pm > month and distance == -1:
            if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
                distance = pd + 31 - day
                break
            elif month == 4 or month == 6 or month == 9 or month == 11:
                distance = pd + 30 - day
                break
            
            else:
                distance = pd + 28 - day
                break
    return distance


def checkDay():
    d = date.today()
    x = calendar.day_name[d.weekday()]
    day = {'Monday':'วันจันทร์', 
           'Tuesday':'วันอังคาร',
           'Wednesday':'วันพุธ',
           'Thursday':'วันพฤหัส',
           'Friday':'วันศุกร์',
           'Saturday':'วันเสาร์',
           'Sunday':'วันอาทิตย์'}
        
    return day[x]