from .models import UserProfile

class GetInformation:
    @classmethod
    def get_user_profile(cls, id):
        user_profile = UserProfile.objects.get(pk=id)
        return user_profile
