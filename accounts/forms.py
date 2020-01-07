from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True)
    alternate_email = forms.EmailField(max_length=254, required=False, help_text=
                'Preferably at least one of your email addresses on record will be'+
                 'a non-edu address (e.g., @gmail.com, @yahoo.com).')
    birth_date = forms.DateField(label='Birth Date',
        help_text='Required. Format: YYYY-MM-DD')
    preferred_name = forms.CharField(max_length=30, required=False,
                            help_text='What would you like us to call you?')

    class Meta:
            model = User
            fields = ('username', 'first_name', 'last_name','password1', 'password2',
                 'email','birth_date' ,'alternate_email', 'preferred_name',)

    def save(self,commit=True):
        user = forms.ModelForm.save(self,commit=False)
        for key,value in self.cleaned_data.items():
            user.__dict__[key] = value
        if commit:
            user.save()
        return user
