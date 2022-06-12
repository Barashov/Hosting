from .models import UserProfile

class GetInformation:
    @classmethod
    def get_file(cls, id):
        user_profile = UserProfile.objects.get(pk=id)
        return user_profile
    @classmethod
    def is_have_profile(cls, user):
        if UserProfile.objects.filter(user=user).exists():
            return True
        else:
            return False
    @classmethod
    def get_profile(cls, user):
        profile = UserProfile.objects.get(user=user)
        return profile