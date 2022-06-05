from django import forms
from innovator.models import Idea
from myadmin.models import Profile


class IdeaForm(forms.ModelForm):
	class Meta:
		model = Idea
		#fields = '__all__'
		exclude = ['user']


class PhotoUploadForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_photo',) 