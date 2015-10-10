from   django.shortcuts                    import render
from   .models                             import Profile, Pony, Url
from   .forms                              import RegistrationForm, ProfileForm
from   django.contrib.auth.decorators      import login_required
from   django.forms.models                 import inlineformset_factory
from   registration.backends.default.views import RegistrationView as BaseRegistrationView
import random


class RegistrationView(BaseRegistrationView):

    form_class = RegistrationForm

    def register(self, request, **cleaned_data):
        return super(RegistrationView, self).register(request, **cleaned_data['registration'])

    def form_valid(self, request, form):
        self.form = form
        return super(RegistrationView, self).form_valid(request, form)

    def get_success_url(self, request=None, user=None):
        self.form.save(user = user)
        return super(RegistrationView, self).get_success_url(request, user)


def members(request):
    users = list(Profile.objects.get_active_users())
    random.shuffle(users)

    return render(request, 'members.html', {
        'profiles': users,
    })


@login_required
def profile(request):
    try:
        profile = Profile.objects.get(user = request.user.id)
    except:
        profile = Profile()
        profile.user = request.user

    # Profile pony
    PonyFormset = inlineformset_factory(Profile, Pony, fields=('pony','message',))
    ponies = PonyFormset(instance = profile)

    # Profile URL
    UrlFormset = inlineformset_factory(Profile, Url, fields=('url',))
    urls = UrlFormset(instance = profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance = profile)
        ponies = PonyFormset(request.POST, instance = profile)
        urls = UrlFormset(request.POST, instance = profile)
        if form.is_valid():
            form.save()
            ponies.save()
            form = ProfileForm(instance = profile)
            ponies = PonyFormset(instance = profile)
            urls = UrlFormset(instance = profile)
    else:
        form = ProfileForm(instance = profile)
        ponies = PonyFormset(instance = profile)
        urls = UrlFormset(instance = profile)

    return render(request, 'profile.html', {
        'profile': profile,
        'form':    form,
        'ponies':  ponies,
        'urls':    urls,
    })
