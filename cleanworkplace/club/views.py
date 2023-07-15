from django.http import HttpResponse
from django.shortcuts import render

import place
from club.models import Club


def index(request):
    club = Club.objects.all()

    context = {
        'club': club,
        'title': 'Главная страница',
        'club_selected': 0,
    }

    return render(request, 'club/index.html', context=context)


def show_club(request, club_id):
    club = Club.objects.all()
    context = {
        'club': club,
        'title': 'клубы',
        'club_selected': club_id,
    }

    return render(request, 'club/club.html', context=context)
