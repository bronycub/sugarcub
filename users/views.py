from django.shortcuts    import render, redirect
from django.contrib.auth import authenticate
from django.shortcuts    import render
from .models             import Profile
from .forms              import SignupForm

def members(request):
    return render(request, 'members.html', {
        'profiles': Profile.objects.all(),
    })

def signup(request):
    if request.method == 'POST':
        form = SignupForm(data = request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
            if user is not None:
                if user.is_active:
                    login(request, user)
            return redirect('users:signup_success')

    else:
        form = SignupForm()

    return render(request, 'auth/signup.html', {
        'form' : form,
    })

def signup_success(request):
    return render(request, 'auth/signup_success.html')

