from django.shortcuts                    import render
from .models                             import Profile, Pony
from .forms                              import RegistrationForm, ProfileForm
from django.contrib.auth.decorators      import login_required
from django.forms.models                 import modelformset_factory
from registration.backends.default.views import RegistrationView as BaseRegistrationView


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
    return render(request, 'members.html', {
        'profiles': Profile.objects.filter(user__is_active = True),
    })


@login_required
def profile(request):
    try:
        profile = Profile.objects.get(user = request.user.id)
    except:
        profile = Profile()
        profile.user = request.user

    ponies = modelformset_factory(Pony, fields = ('pony', 'message'))

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance = profile)
        if form.is_valid():
            form.save()
            form = ProfileForm(instance = profile)
    else:
        form = ProfileForm(instance = profile)

    return render(request, 'profile.html', {
        'profile': profile,
        'form':    form,
        'ponies':  ponies,
    })
