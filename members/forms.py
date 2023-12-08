from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from myblog.models import Profile

class ProfilePageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio','profile_pic','web_url','facebook_url','instagram_url','twitter_url','github_url','linkedin_url')
        labels = {
            'bio':'Add your Bio (required)',
            'profile_pic':'Add your profile picture:\n',
            'web_url':'Add your website:',
            'facebook_url':'Add your facebook account:',
            'instagram_url':'Add your instagram account:',
            'twitter_url':'Add your twitter account:',
            'github_url':'Add your github account:',
            'linkedin_url':'Add your linkedin account:',

        }
        widgets = {
            'bio' : forms.Textarea(attrs={'class':'form-control bg-dark text-light','placeholder':'Add you bio here'}),
            'web_url' : forms.TextInput(attrs={'class':'form-control bg-dark text-light','placeholder':'http://www.example.com'}),
            'facebook_url' : forms.TextInput(attrs={'class':'form-control bg-dark text-light','placeholder':'http://facebook.com/user_name'}),
            'instagram_url' : forms.TextInput(attrs={'class':'form-control bg-dark text-light','placeholder':'http://instagram.com/user_name'}),
            'twitter_url' : forms.TextInput(attrs={'class':'form-control bg-dark text-light','placeholder':'http://twitter.com/user_name'}),
            'github_url' : forms.TextInput(attrs={'class':'form-control bg-dark text-light','placeholder':'http://github.com/user_name'}),
            'linkedin_url' : forms.TextInput(attrs={'class':'form-control bg-dark text-light','placeholder':'http://linkedin.com/user_name'}),
        }



class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control bg-dark text-light','placeholder':'Enter Mail-id'}))
    first_name = forms.CharField(max_length = 100,widget=forms.TextInput(attrs={'class':'form-control bg-dark text-light','placeholder':'Enter First Name'}))
    last_name = forms.CharField(max_length = 100,widget=forms.TextInput(attrs={'class':'form-control bg-dark text-light','placeholder':'Enter Last Name'}),required=False)

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']
        labels = {
            'username':'',
            'first_name':'',
            'last_name':'',
            'email':'',
            'password1':'',
            'password2':'',
        }

    def __init__(self,*args,**kwargs):
        super(SignUpForm,self).__init__(*args,**kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control bg-dark text-light'
        self.fields['username'].widget.attrs['placeholder'] = 'Enter Username'
        self.fields['password1'].widget.attrs['class'] = 'form-control bg-dark text-light'
        self.fields['password1'].widget.attrs['placeholder'] = 'Enter Password'
        self.fields['password2'].widget.attrs['class'] = 'form-control bg-dark text-light'
        self.fields['password2'].widget.attrs['placeholder'] = 'Enter Password again'


class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control bg-dark text-light','placeholder':'example@mail.com'}))
    first_name = forms.CharField(max_length = 100,widget=forms.TextInput(attrs={'class':'form-control bg-dark text-light','placeholder':'elijah'}))
    last_name = forms.CharField(max_length = 100,widget=forms.TextInput(attrs={'class':'form-control bg-dark text-light','placeholder':'Mikaelson'}),required=False)

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password']

    def __init__(self,*args,**kwargs):
        super(EditProfileForm,self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control bg-dark text-light'


class PasswordChangingForm(PasswordChangeForm):
    old_password =  forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control bg-dark text-light','type':'password'}))
    new_password1 = forms.CharField(max_length = 100,widget=forms.PasswordInput(attrs={'class':'form-control bg-dark text-light','type':'password'}))
    new_password2 = forms.CharField(max_length = 100,widget=forms.PasswordInput(attrs={'class':'form-control bg-dark text-light','type':'password'}))

    class Meta:
        model = User
        fields = ['old_password','new_password1','new_password2']
