from django import forms
from django.forms import ModelForm
from .models import Post,Category,Comment


choices = Category.objects.all().values_list('name','name')
choice_list = [item for item in choices]
#choices = [('coding','coding'),('sports','sports'),('entertainment','entertaiment')]
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title','author','category','body','header_image')
        labels = {
            'title':'',
            'body':'',
            'category':'',
            'header_image':'Upload image here'
        }
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control bg-dark text-light','placeholder':'Title of Blog'}),
            'author' : forms.TextInput(attrs={'class':'form-control bg-dark text-light','value':'','type':'hidden','id':'author_field'}),
            #'author' : forms.Select(attrs={'class':'form-control'}),
            'category' : forms.Select(choices=choice_list,attrs={'class':'form-control bg-dark text-light'}),
            'body' : forms.Textarea(attrs={'class':'form-control bg-dark text-light'}),
        }


class EditForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title','body','header_image')

        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control bg-dark text-light','placeholder':'Title of Blog'}),
            #'title_tag' : forms.TextInput(attrs={'class':'form-control','placeholder':'Title to be shown in head'}),
            #'author' : forms.Select(attrs={'class':'form-control'}),
            'body' : forms.Textarea(attrs={'class':'form-control bg-dark text-light'}),
            #'snippet' : forms.Textarea(attrs={'class':'form-control'})
        }



class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('name','body')

        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control ','placeholder':'Name','id':'comment_name'}),
            'body' : forms.Textarea(attrs={'class':'form-control'}),
        }

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ('name',)
        labels = {
            'name':'',
        }
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control bg-dark text-light','placeholder':'Category',"onkeyup":"this.value = this.value.toLowerCase();"}),
        }