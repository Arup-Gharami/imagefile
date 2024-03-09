from django import forms
from uploadimageapp.models import ImageUploadModel

class ImageuploadForm(forms.ModelForm):
    class Meta:
        model = ImageUploadModel
        fields = '__all__'

