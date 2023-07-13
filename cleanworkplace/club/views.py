from django.http import HttpResponse
from django.shortcuts import render

from club.models import Club


def index(request):
    club = Club.objects.all()
    context = {
        'club': club,
        'title': 'Главная страница'
    }
    return render(request, 'club/index.html', context=context)
