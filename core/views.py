from   django.shortcuts import render
from   django.conf      import settings
from   .models          import Friend, Quote
from   users.models     import Profile
from   django.views.decorators.cache import cache_page
import urllib.request
import re

@cache_page(60 * 0.5)
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

@cache_page(60 * 15)
def agenda(request):
    return render(request, 'agenda.html')

@cache_page(60 * 15)
def map(request):
    return render(request, 'map.html', {
        'fillPage':        True,
        'profiles':        Profile.objects.filter(user__is_active = True),
        'OSM_TILE_SERVER': settings.OSM_TILE_SERVER,
    })

@cache_page(60 * 15)
def friends(request):
    friends = Friend.objects.all()

    if friends.count() > 2:
        friend_width = 4
    elif friends.count() == 2:
        friend_width = 6
    else:
        friend_width = 12

    return render(request, 'friends.html', {
        'friends':     friends,
        'friendWidth': friend_width,
    })
