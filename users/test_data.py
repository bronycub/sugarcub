from .           import models
from model_mommy import mommy


def create_profiles():
    profiles = mommy.make(models.Profile, enabled = True, _quantity = 4)

    for i in range(0, 3):
        profiles[i].user.username = 'profile' + str(i)

    profiles[0].user.is_active = False
    profiles[0].enabled        = False

    profiles[1].user.is_active = True
    profiles[1].enabled        = False

    profiles[2].enabled        = False

    for i in range(0, 3):
        profiles[i].user.username = 'profile' + str(i)
        profiles[i].save()

    return profiles
