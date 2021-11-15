from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def timeinfo(request):
    date=datetime.datetime.now()
    s='<h1>Hello friend Good Evening!!!</h1><hr>'
    msg=s+'<h1>Now server time is'+str(date)+'</h1>'
    return HttpResponse(msg)
