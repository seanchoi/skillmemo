from django import forms
from .models import *


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photos
        fields = ('files', )

class PhotoForm02(forms.ModelForm):
    class Meta:
        model = Photos02
        fields = ('files', )

class PhotoForm03(forms.ModelForm):
    class Meta:
        model = Photos03
        fields = ('files', )
