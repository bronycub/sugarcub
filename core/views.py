from   django.shortcuts import render
import urllib.request
import re

def home(request):
	irc = str(urllib.request.urlopen('http://www.art-software.fr/files/lastlog_bronycub.php').read(), encoding='utf-8')
	irc = re.sub(r'(.*(kick|ban).*)',          r'<span class="text-warning">\1</span>', irc)
	irc = re.sub(r'(&lt;[a-zA-Z0-9\-_]*&gt;)', r'<span class="text-primary">\1</span>', irc)
	irc = re.sub(r'(.*\*\*\*.*)',              r'<span class="text-info">\1</span>',    irc)

	return render(request, 'home.html', {
		'irc': irc,
	})

def agenda(request):
    return render(request, 'agenda.html')

def map(request):
    return render(request, 'map.html')

def friends(request):
    return render(request, 'friends.html')
