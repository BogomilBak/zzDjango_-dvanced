from django import forms
from django.forms import modelform_factory

from web.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"


ProfileForm2 = modelform_factory(Profile, )