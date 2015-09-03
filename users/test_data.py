from .           import models
from model_mommy import mommy


def create_profiles():
    profiles = mommy.make(models.Profile, enabled = True, _quantity = 4)

    profiles[0].user.is_active = False
    profiles[0].enabled        = False

    profiles[1].user.is_active = True
    profiles[1].enabled        = False

    profiles[2].user.is_active = False
    profiles[2].enabled        = True

    profiles[3].user.is_active = True
    profiles[3].enabled        = True

    profiles[3].user.username  = 'Fluttershy_profile'
    profiles[3].bio            = 'profile_bio'

    for i in range(0, 4):
        profiles[i].user.save()
        profiles[i].save()

    return profiles
