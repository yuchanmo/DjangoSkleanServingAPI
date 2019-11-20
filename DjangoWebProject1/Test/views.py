from django.shortcuts import render
from django.http import HttpResponse

def test1(request):
    return HttpResponse('test 중입니다')
# Create your views here.
