
from django.http import HttpResponse
from django.template import loader
from chanting.time import monk_day
from chanting.time import checkDay
from django.shortcuts import render
from .models import praying, prayingset


# def main(request):

#     if monk_day():
#         s = "วันนี้วันพระ"
    
#     else:
#         s = ""
#     context = {
#         "monk" : s
#     }
#     return render(request,"main.html",context)

def main(request):
    context = {}

    '''if monk_day():
        s = "วันนี้วันพระ"

    else:
        s = ""    '''
    n = monk_day()
    if(n == 0):
        context = {'monk' : "วันนี้วันพระ"}
    elif(n == 1):
        context = {'monk' : "พรุ่งนี้วันพระ"}
    elif(n == -1):
        context = {'monk' : "หมดปีแล้วจ้า:)"}
    else:
        context = {'monk' : "อีก " + str(n) + " วันจะถึงวันพระ"}
    return render(request,"main.html",context)


def chanting(request,title):
    if(praying.objects.filter(title = title)):
        ch = praying.objects.get(title = title)
        content = ch.content
        context ={
            "title" : title,
            "content" : content
        }
    else:
        context = {
            "title" : title,
            "content" : "ไม่พบข้อมูลในคลังบทสวด"
        }
    return render(request,"chanting.html",context)

def suadPrajum(request):
    context={'day': checkDay()}
    return render(request, "suadPrajum.html",context)

def sevenday(request):
    context = {
        "monday" : 'วันจันทร์',
        "tuesday" : 'วันอังคาร',
        "wednesday" : 'วันพุธ',
        "thursday" : 'วันพฤหัส',
        "friday" : 'วันศุกร์',
        "saturday" : 'วันเสาร์',
        "sunday" : 'วันอาทิตย์',
        "n" : '1',
    }
    return render(request, "7day.html",context)
def totalD(request):
    context = {
        "ok" : "บทสวดประจำวันออกพรรษา",
        "khao" : 'บทสวดประจำวันเข้าพรรษา',
        "maka" : 'บทสวดวันมาฆบูชา',
        "visaka" : "บทสวดวันวิสาขบูชา",
        "asa" : "บทสวดวันอาสาฬหบูชา",
        "atha" : "บทสวดวันอัฏฐมีบูชา",
        "n" : '1',
    } 
    return render(request, "totalD.html",context)
def set(request,title,n):
    context = {}
    if(prayingset.objects.filter(title = title)):
        context = {'ptitle' : title}
        ps = prayingset.objects.get(title = title)
        prlist = ps.set.all()
        n = int(n)
        context.update( {"next" : str(n+1)} )
        n = n-1
        for i in range (n*9,len(prlist)):
            if(i - (n*9) == 9):
                break
            key = "p" + str( (i % 9) + 1)
            context.update( {key : prlist[i].title})
            if(i+1 < len(prlist)):
                context.update({"continue" : "continue"})
        if(n > 0) :
            context.update({"back" : str(n)})

    return render(request,"set.html",context)

