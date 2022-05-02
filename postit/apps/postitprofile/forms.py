from django import forms
from .models import PostitProfile

class postitprofileform(forms.ModelForm):
	class Meta:
		model = PostitProfile
		fields = ('avatar',) 
