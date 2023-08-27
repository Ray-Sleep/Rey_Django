from django.shortcuts import render

# 在这里创建你的视图.

from django.shortcuts import render

from .models import Post


def index(request):
    context = { 'news_list': Post.objects.all() }
    return render(request, 'news/index.html', context=context)
