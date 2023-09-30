from django.shortcuts import render, HttpResponse, redirect
import requests

from news.models import UserInfo


def login(req):
    print(req.POST)

    if req.method == 'GET':
        return render(req, 'first_login.html')

    username = req.POST.get('user')
    number = req.POST.get('number')
    password = req.POST.get('pwd')

    # 注册
    """
    检测用户名、邮箱、电话是否重复
    """
    if UserInfo.objects.filter(name=username).exists() and UserInfo.objects.filter(number=number).exists():
        return HttpResponse('注册失败，用户名或邮箱重复')
    else:
        UserInfo.objects.create(name=username, number=number, password=password)

    # 登入
    """检测用户名、邮箱、电话 是否存在数据库"""
    if number == '':
        pass

    # if username == 'admin' and password == '123':
    #     return HttpResponse('登录成功')
    return HttpResponse('登录成功')


def user_list(req):
    # 在 app 目录下的 templates 目录寻找 user_list.html 模板文件.(根据app的注册顺序，逐一去templates目录中查找）
    # 注意，这里使用的是相对路径，相对于 app 目录.
    data_list = UserInfo.objects.all()
    return render(req, 'user_list.html',{'data_list':data_list})


def something(req):
    # context = {'news_list': Post.objects.all()}
    headers = {
        # 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.81',
        # 'Accept-Encoding':'gzip, deflate',
        # 'Accept - Language' : 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'
    }
    url = {"http://www.chinaunicom.com/api/article/NewsByIndex/2/2023/09/news"}
    res = requests.get(url=url, headers=headers)
    data_list = res.json()
    print(data_list)

    return render(req, 'news/news.html')
    # return render(req, 'news/news.html', {'news_list': data_list})
    # return redirect('http://www.baidu.com')


def test(req):
    # 获得请求方式 （GET / POST）
    print(req.method)
    # 获取在 URL 上传递的参数 ( /something/?n1=123&n2=666 )
    print(req.GET)
    # 在请求体中提交数据
    print(req.POST)

    # 内容字符串 返回给 请求者
    # return HttpResponse('返回内容')

    # 重定向 让服务器
    return redirect('http://www.baidu.com')


def user_add(req):
    # 字符串
    name = 'Rey'
    # 列表
    roles = ['admin', 'ceo']
    # 字典
    user_info = {"name": 'Rey', "salary": 10000, "role": 'ceo'}
    # 列表套字典
    data_list = [
        {"name": 'Rey', "salary": 10000, "role": 'ceo'},
        {"name": 'Tom', "salary": 8000, "role": 'admin'},
        {"name": 'Jerry', "salary": 3000, "role": '保安'}
    ]
    return render(req, 'user_add.html', {"n1": name, "n2": roles, "n3": user_info, "n4": data_list})
