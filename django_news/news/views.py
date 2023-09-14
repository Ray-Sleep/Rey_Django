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
    return render(request, 'user_add.html')