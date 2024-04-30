from django.shortcuts import render
from .models import Room, Employees

# Create your views here.
# rooms = [
#     {'id': 1, 'name': 'Lets Develop python'},
#     {'id': 2, 'name': 'Design with me'},
#     {'id': 3, 'name': 'Frontend developers'},
    
# ]


def home(request):
    rooms = Room.objects.all()
    employees = Employees.objects.all()
    
    context = {'rooms': rooms, 'employees':employees}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'base/room.html', context)

def employees(request):
    employees = Employees.objects.all()
    return render(request, 'base/home.html')
