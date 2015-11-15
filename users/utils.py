from django.contrib.auth          import get_user_model
from django.contrib.auth.backends import ModelBackend


class EmailOrUsernameModelBackend(ModelBackend):
    ''' Authenticate user by username or email '''

    def authenticate(self, username = None, password = None):
        User = get_user_model()

        try:
            user = User.objects.get(email = username)
            if user.check_password(password):
                return user
            else:
                return None
        except User.DoesNotExist:
            return None
