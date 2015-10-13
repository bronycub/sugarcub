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
    # Get the user's profile
    try:
        profile = Profile.objects.get(user = request.user.id)
    except:
        profile = Profile()
        profile.user = request.user

    # inline formset for profile's pony
    ponyformset = inlineformset_factory(Profile, Pony, fields = ('pony', 'message',), extra = 0)

    # inline formset for profile's url
    urlformset = inlineformset_factory(Profile, Url, fields = ('url',), extra = 0)

    if request.method=='POST':

        # To add a new row for pony (avoid using JS)
        if 'add_pony' in request.POST:
            cp = request.POST.copy()
            cp['pony-TOTAL_FORMS'] = int(cp['pony-TOTAL_FORMS'])+ 1

            form = ProfileForm(request.POST, request.FILES, instance = profile)
            ponies = ponyformset(cp, prefix = "pony")
            urls = urlformset(request.POST, instance = profile, prefix='url')

        # To add a new row for url (avoid using JS)
        if 'add_url' in request.POST:
            cp = request.POST.copy()
            cp['url-TOTAL_FORMS'] = int(cp['url-TOTAL_FORMS'])+ 1

            form = ProfileForm(request.POST, request.FILES, instance = profile)
            ponies = ponyformset(request.POST, instance = profile, prefix = "pony")
            urls = urlformset(cp, prefix='url')

        # When submitting information
        if 'submit' in request.POST:
            form = ProfileForm(request.POST, request.FILES, instance = profile)
            ponies = ponyformset(request.POST, instance = profile, prefix = "pony")
            urls = urlformset(request.POST, instance = profile, prefix = "url")

            if form.is_valid():
                form.save()

                form = ProfileForm(instance = profile)

            if ponies.is_valid():
                ponies.save()

                ponies = ponyformset(instance = profile, prefix = "pony")

            if urls.is_valid():
                urls.save()

                urls = urlformset(instance = profile, prefix = "url")

    else:
        form = ProfileForm(instance = profile)
        ponies = ponyformset(instance = profile, prefix = "pony")
        urls = urlformset(instance = profile, prefix = "url")

    return render(request, 'profile.html', {
        'profile': profile,
        'form':    form,
        'ponies':  ponies,
        'urls':    urls,
    })
