import threading

from django.http import HttpResponse
from django.shortcuts import render

import place
from club.models import Club, Picture

t = threading.Thread(target=place.get_image)
t.setDaemon(True)
t.start()


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
    pictures = Picture.objects.filter(camera__club_id=club_id).order_by('-time')
    context = {
        'club': club,
        'picture': pictures,
        'title': 'клубы',
        'club_selected': club_id,
    }

    return render(request, 'club/club.html', context=context)
