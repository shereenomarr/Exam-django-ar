from django import forms
from django.contrib.auth.models import User

class usercreationForm(forms.ModelForm):
    username= forms.CharField(max_length=30)
    email=forms.EmailField()
    first_name=forms.CharField()
    last_name= forms.CharField()
    passwrd=forms.CharField() 
     

    class Meta:
        model=User
        fields=('username','email','first_name','last_name','password')

    def clean_password2(self):
        cd=self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('password does not match')
        return cd['password2']        