from django.shortcuts               import render, redirect
from django.contrib.auth            import authenticate, login
from django.shortcuts               import render
from .models                        import Profile, Pony
from .forms                         import SignupForm, ProfileForm
from django.contrib.auth.decorators import login_required
from django.forms.models            import modelformset_factory

def members(request):
    return render(request, 'members.html', {
        'profiles': Profile.objects.all(),
    })

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            user = authenticate(
                username = request.POST.get('user-username'),
                password = request.POST.get('user-password1')
            )
            if user is not None and user.is_active:
                login(request, user)

            return redirect('users:signup_success')

    else:
        form = SignupForm()

    return render(request, 'auth/signup.html', {
        'form' : form,
    })

def signup_success(request):
    return render(request, 'auth/signup_success.html')

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
