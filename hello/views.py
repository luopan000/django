from django.shortcuts import render
from django.http import HttpResponse
from hello.models import User
# Create your views here.
# class Users:
#     def __init__(self,name,pwd):
#         self.name = name
#         self.pwd = pwd

def index(request):
    return  render(request,'taopiaopiao.html')


def users(request):
    #模拟保存两条数据
    mayun = User(username='马云', age = 18)
    mayun.save()
    mahuateng = User(username='马化腾', age=18)
    mahuateng.save()
    #查询返回给前端
    users = User.objects.all()
    return render(request,'user_logo_in.html',{'users':users})