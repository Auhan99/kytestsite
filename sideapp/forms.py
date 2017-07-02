from django import forms
from .models import SignUp
class SignUpForms(forms.ModelForm):
    class Meta:
        model =SignUp
        fields =["name","email",]
    
    
    def clean_name(self):
        name=self.cleaned_data.get("name")
        return name
   
    
   