from django                     import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms  import UserCreationForm
from multiform                  import MultiModelForm
from .models                    import Profile
from collections                import OrderedDict

class SignupProfileForm(forms.ModelForm):

    class Meta:
        model  = Profile
        fields = ['bio', 'gravatar', 'avatar', 'phone', 'birthday', 'address']

class SignupForm(MultiModelForm):
    base_forms = [
        ('user',    UserCreationForm),
        ('profile', SignupProfileForm),
    ]

    def dispatch_init_instance(self, name, instance):
        if name == 'profile':
            return instance
        return super(SignupForm, self).dispatch_init_instance(name, instance)

    def save(self, commit=True):
        """Save both forms and attach the user to the profile."""
        instances = super(SignupForm, self).save(commit=False)
        instances['profile'].user = instances['user']
        if commit:
            for instance in instances.values():
                instance.save()
        return instances
