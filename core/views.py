from   django.shortcuts  import render
from   django.conf       import settings
from   .models           import Friend, Quote
from   users.models      import Profile
from   django.core.cache import cache
import requests
import re
import random


def home(request):

    irc = cache.get('irc_log')
    if not irc:
        try:
            irc = requests.get('http://www.art-software.fr/files/lastlog_bronycub.php').text
            irc = re.sub(r'(.*(kick|ban).*)',          r'<span class="text-warning">\1</span>', irc)
            irc = re.sub(r'(&lt;[a-zA-Z0-9\-_]*&gt;)', r'<span class="text-primary">\1</span>', irc)
            irc = re.sub(r'(.*\*\*\*.*)',              r'<span class="text-info">\1</span>',    irc)
            cache.set('irc_log', irc)
        except:
            irc = ''

    quotes = list(Quote.objects.all())
    random.shuffle(quotes)

    return render(request, 'home.html', {
        'irc':      irc,
        'quotes':   quotes,
        'birthday': Profile.objects.get_birthday(),
        'new':      Profile.objects.get_new_members(),
        'list_new': len(Profile.objects.get_new_members()),
    })


def agenda(request):

    return render(request, 'agenda.html')


def map(request):

    return render(request, 'map.html', {
        'fillPage':        True,
        'profiles':        Profile.objects.get_active_users(),
        'OSM_TILE_SERVER': settings.OSM_TILE_SERVER,
    })


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


def bad_request(request):
    return render(request, 'errors/bad_request.html')


def permission_denied(request):
    return render(request, 'errors/permission_denied.html')


def page_not_found(request):
    return render(request, 'errors/page_not_found.html')


def server_error(request):
    return render(request, 'errors/server_error.html')
