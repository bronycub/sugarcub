from   django.shortcuts               import render, redirect
from   django.contrib                 import auth
from   django.contrib.auth.decorators import login_required
from   django.contrib.auth            import authenticate
from   .models                        import Friend
import urllib.request
import re

def home(request):
    try:
        irc = str(urllib.request.urlopen('http://www.art-software.fr/files/lastlog_bronycub.php').read(), encoding='utf-8')
        irc = re.sub(r'(.*(kick|ban).*)',          r'<span class="text-warning">\1</span>', irc)
        irc = re.sub(r'(&lt;[a-zA-Z0-9\-_]*&gt;)', r'<span class="text-primary">\1</span>', irc)
        irc = re.sub(r'(.*\*\*\*.*)',              r'<span class="text-info">\1</span>',    irc)
    except:
        irc = ''

    return render(request, 'home.html', {
        'irc': irc,
    })

def agenda(request):
    return render(request, 'agenda.html')

def map(request):
    return render(request, 'map.html', {
        'fillPage': True,
        'profiles': Profile.objects.all(),
    })

def friends(request):
    friends     = Friend.objects.all()

    if friends.count() > 2:
        friendWidth = 4
    elif friends.count() == 2:
        friendWidth = 6
    else:
        friendWidth = 12

    return render(request, 'friends.html', {
        'friends': friends,
        'friendWidth': friendWidth,
    })
