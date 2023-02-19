# django_project/users/forms.py
from django import forms
from django.contrib.auth.forms import (UserCreationForm, AuthenticationForm,
                                       SetPasswordForm, UserChangeForm)
from django.contrib.auth import get_user_model
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox, ReCaptchaV3

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(help_text='A valid email address, please.', required=True)
     
    password1 = forms.CharField(help_text=None, widget=forms.PasswordInput(
    attrs={'class':'form-control','type':'password', 'name': 'password','placeholder':'Password'}),
    label='')

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'username',  'email', 'picture','description', 'password1', 'password2']

    # def save(self, commit=True):
    #     user = super(UserRegistrationForm, self).save(commit=False)
    #     user.email = self.cleaned_data['email']
    #     if commit:
    #         user.save()
    #     return user


class loginForm():
    pass

class loginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(loginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Username or Email'}),
        label="Username or Email")

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password'}))
    
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())


class profileForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email', 'picture', 'description']


class changePasswordForm(SetPasswordForm):
    class Meta:
        model = get_user_model()
        fields = '__all__'