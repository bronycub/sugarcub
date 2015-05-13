from   django.shortcuts import render
from   django.conf      import settings
from   .models          import Friend, Quote
from   users.models     import Profile
import urllib.request
import re


def home(request):
    try:
        irc = str(urllib.request.urlopen('http://www.art-software.fr/files/lastlog_bronycub.php').read(),
                encoding='utf-8')
        irc = re.sub(r'(.*(kick|ban).*)',          r'<span class="text-warning">\1</span>', irc)
        irc = re.sub(r'(&lt;[a-zA-Z0-9\-_]*&gt;)', r'<span class="text-primary">\1</span>', irc)
        irc = re.sub(r'(.*\*\*\*.*)',              r'<span class="text-info">\1</span>',    irc)
    except:
        irc = ''

    return render(request, 'home.html', {
        'irc': irc,
        'quotes': Quote.objects.all,
    })


def agenda(request):
    return render(request, 'agenda.html')


def map(request):
    return render(request, 'map.html', {
        'fillPage':        True,
        'profiles':        Profile.objects.filter(user__is_active = True),
        'OSM_TILE_SERVER': settings.OSM_TILE_SERVER,
    })


def friends(request):
    friends = Friend.objects.all()

    if friends.count() > 2:
        friendWidth = 4
    elif friends.count() == 2:
        friendWidth = 6
    else:
        friendWidth = 12

    return render(request, 'friends.html', {
        'friends':     friends,
        'friendWidth': friendWidth,
    })
