from .models import Sites

class GetInformation():
    @classmethod
    def get_file_name(cls, id):
        file_name = Sites.objects.get(pk=id).html_file
        return file_name
        