from django import forms
from lost_found import models

class CreateArticle(forms.ModelForm):
	class Meta:
		model=models.lost_found
		fields=['item_name','item_description','slug_path','image']