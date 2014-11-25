from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def agenda(request):
    return render(request, 'agenda.html')

def map(request):
    return render(request, 'map.html')

def friends(request):
    return render(request, 'friends.html')
