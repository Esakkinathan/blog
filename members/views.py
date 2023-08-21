from django.shortcuts import render,get_object_or_404
from django.views import generic
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from .forms import SignUpForm,EditProfileForm,PasswordChangingForm,ProfilePageForm
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from myblog.models import Profile,Post
# Create your views here.

from django.views.decorators.csrf import csrf_exempt

class ShowProfileView(generic.DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'
    
    def get_context_data(self,*args,**kwargs):
        #users = Profile.objects.all()
        context = super(ShowProfileView,self).get_context_data(*args,**kwargs)
        page_user=get_object_or_404(Profile,id=self.kwargs['pk'])
        posts = Post.objects.filter(author=self.kwargs['pk']).values()
        #print(posts)
        context['page_user'] = page_user
        context['posts'] = posts
        return context
@csrf_exempt
class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')
    
    def get_object(self):
        return self.request.user

class PasswordChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    template_name = 'registration/change_password.html'
    #success_url = reverse_lazy('home')
    
def password_success(request):
    return render(request,'registration/password_success.html',{})

class EditProfileView(generic.UpdateView):
    model = Profile
    form_class=ProfilePageForm
    template_name = "registration/edit_profile_page.html"
    #fields = ['profile_pic','bio','web_url','facebook_url','instagram_url','twitter_url','github_url']
    success_url = reverse_lazy('home')
    
class CreateProfileView(generic.CreateView):
    model = Profile
    form_class=ProfilePageForm
    template_name = "registration/create_user_profile.html"
    #fields = "__all__"
    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)
