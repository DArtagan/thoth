from django.forms import ModelForm
from scribe.models import Upload

class UploadImage(ModelForm):
    class Meta:
        model = Upload
        fields = ['image']
