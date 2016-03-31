from   django.shortcuts                    import render
from   .                                   import models, forms
from   django.contrib.auth.decorators      import login_required
from   django.forms.models                 import inlineformset_factory
from   registration.backends.default.views import RegistrationView as BaseRegistrationView
import random
import logging


class RegistrationView(BaseRegistrationView):

    form_class = forms.RegistrationForm

    def register(self, request, **cleaned_data):
        logging.error('test')
        return super().register(request, **cleaned_data['registration'])

    def form_valid(self, request, form):
        self.form = form
        logging.error(form.__dict__)
        return super().form_valid(request, form)

    def get_success_url(self, request=None, user=None):
        self.form.save(user = user)
        return super().get_success_url(request, user)


def members(request):

    users = list(models.Profile.objects.get_active_users())
    random.shuffle(users)

    return render(request, 'members.html', {
        'profiles': users,
    })


@login_required
def profile(request):

    # Get the user's profile
    try:
        profile = models.Profile.objects.get(user = request.user.id)
    except:
        profile = models.Profile()
        profile.user = request.user

    # inline formset for profile's pony
    ponyformset = inlineformset_factory(
        models.Profile, models.UserPony, form = forms.UserPonyForm, fields = ('pony', 'message',), extra = 0
    )

    # inline formset for profile's url
    urlformset = inlineformset_factory(models.Profile, models.UserUrl, fields = ('icon', 'url',), extra = 0)

    if request.method == 'POST':

        # To add a new row for pony (avoid using JS)
        if 'add_pony' in request.POST:
            cp = request.POST.copy()
            cp['pony-TOTAL_FORMS'] = int(cp['pony-TOTAL_FORMS']) + 1

            form = forms.ProfileForm(request.POST, request.FILES, instance = profile)
            ponies = ponyformset(cp, prefix = 'pony')
            urls = urlformset(request.POST, instance = profile, prefix='url')

        # To add a new row for url (avoid using JS)
        if 'add_url' in request.POST:
            cp = request.POST.copy()
            cp['url-TOTAL_FORMS'] = int(cp['url-TOTAL_FORMS']) + 1

            form = forms.ProfileForm(request.POST, request.FILES, instance = profile)
            ponies = ponyformset(request.POST, instance = profile, prefix = 'pony')
            urls = urlformset(cp, prefix='url')

        # When submitting information
        if 'submit' in request.POST:
            form = forms.ProfileForm(request.POST, request.FILES, instance = profile)
            ponies = ponyformset(request.POST, instance = profile, prefix = 'pony')
            urls = urlformset(request.POST, instance = profile, prefix = 'url')

            if form.is_valid():
                form.save()

                form = forms.ProfileForm(instance = profile)

            if ponies.is_valid():
                ponies.save()

                ponies = ponyformset(instance = profile, prefix = 'pony')

            if urls.is_valid():
                urls.save()

                urls = urlformset(instance = profile, prefix = 'url')

    else:
        form = forms.ProfileForm(instance = profile)
        ponies = ponyformset(instance = profile, prefix = 'pony')
        urls = urlformset(instance = profile, prefix = 'url')

    return render(request, 'profile.html', {
        'profile': profile,
        'form':    form,
        'ponies':  ponies,
        'urls':    urls,
    })
