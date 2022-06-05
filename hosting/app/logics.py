from .models import Sites

class GetInformation():
    @classmethod
    def get_file_name(cls, id):
        site = Sites.objects.get(pk=id)
        file_name = site.html_file
        return file_name
        