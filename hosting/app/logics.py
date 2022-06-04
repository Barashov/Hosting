from .models import Sites

class GetInformation():
    @classmethod
    def get_all_sites(cls):
        all_sites = Sites.objects.all()
        return all_sites