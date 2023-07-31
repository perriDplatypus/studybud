from django.shortcuts import render
from .models import Room


rooms = [
    {'id':1, 'name':'Lets learn python!'},
    {'id':2, 'name':'Lets learn python!'},
    {'id':3, 'name':'Lets learn python!'},
    {'id':4, 'name':'Lets learn python!'},
    {'id':5, 'name':'Lets learn python!'},
]


def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)


def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'base/room.html', context)


def createRoom(request):
    context = {}
    return render(request, 'base/room_form.html', context)