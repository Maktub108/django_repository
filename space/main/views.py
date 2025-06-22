from django.shortcuts import render
from django.http import HttpResponse

def data_view(request):
    return HttpResponse ('<h1>Многие популярные веб-приложения разработаны с использованием Django, данное приложение предлагает сразу готовый набор инструментов для работы.</h1>')

def test_view(request):
    return HttpResponse ('<h1>Django — это мощный и популярный веб-фреймворк, написанный на языке программирования Python. Он используется для создания веб-приложений и API.</h1>')



