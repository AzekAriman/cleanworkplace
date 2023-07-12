from django.http import HttpResponse
from django.shortcuts import render

menu = [{'title': "КОЛИЗЕЙ", 'url_name': 'about'},
        {'title': "login", 'url_name': 'addpage'},
        ]


def index(request):
    return render(request, 'club/index.html')
