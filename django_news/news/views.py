from django.shortcuts import render

# 在这里创建你的视图.

from django.shortcuts import render

from .models import Post


def index(request):
    context = {'news_list': Post.objects.all()}
    return render(request, 'news/index.html', context=context)


def user_list(request):
    # 在 app 目录下的 templates 目录寻找 user_list.html 模板文件.(根据app的注册顺序，逐一去templates目录中查找）
    # 注意，这里使用的是相对路径，相对于 app 目录.
    return render(request, 'user_list.html')


def user_add(request):
    # 字符串
    name = 'Rey'
    # 列表
    roles = ['admin', 'ceo']
    # 字典
    user_info = {"name":'Rey',"salary":10000,"role":'ceo'}
    # 列表套字典
    data_list = [
        {"name":'Rey',"salary":10000,"role":'ceo'},
        {"name":'Tom',"salary":8000,"role":'admin'},
        {"name":'Jerry',"salary":3000,"role":'保安'}
    ]
    return render(request, 'user_add.html', {"n1": name,"n2":roles,"n3":user_info,"n4":data_list})
