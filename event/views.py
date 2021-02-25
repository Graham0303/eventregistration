from django.shortcuts import render
from .models import Participant

# Create your views here.

def home(request):
    context = {}
    return render(request, 'event/home.html', context)

def success(request):
    context = {}
    return render(request, 'event/success.html', context)

def failure(request):
    context = {}
    return render(request, 'event/failure.html', context)

def register(request):
    context = {}
    if request.method == 'POST':
        p1 = Participant()
        p1.username = request.Post.get('username','-')
        p1.email = request.Post.get('email','-')
        p1.phone = request.Post.get('phone','000')
        p1.institution = request.Post.get('institution','-')

        if len(Participant.objects.all()) > 15:
            return render(request, 'event/failed.html')
        else:
            return render(request, 'event/sucess.html')

    if request.method == 'GET':
        context['username'] = ''
        context['email'] = ''
        context['phone'] = ''
        context['institution'] = ''   
                  
    return render(request, 'event/register.html', context)

def listofparticipants(request):
    context = {}
    return render(request, 'event/listofparticipants.html', context)