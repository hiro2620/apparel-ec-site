from django.contrib.auth.views import LoginView, LogoutView
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, CreateView
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy

from .forms import SigninForm, SignUpForm

class SignInView(LoginView):
    """ログインページ"""
    form_class = SigninForm
    template_name = "users/signin.html"

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.gender = form.cleaned_data.get('gender')
            user.profile.address = form.cleaned_data.get('address')
            user.profile.zipcode = form.cleaned_data.get('zipcode')

            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('shop:home')
    else:
        form = SignUpForm()
    return render(request, 'users/signup.html', {'form': form})

# class SignUpView(CreateView):
#     form_class = SignUpForm
#     template_name = "users/signup.html"
#     success_url = reverse_lazy("shop:home")

#     def form_valid(self, form):
#         user = form.save()
#         login(self.request, user)
#         self.object = user
#         return HttpResponseRedirect(self.get_success_url())

class SignoutView(LoginRequiredMixin, LogoutView):
    """ログアウトページ"""
    template_name = "users/signin.html"

class MypageView(LoginRequiredMixin, TemplateView):
    """マイページ"""
    template_name = "users/mypage.html"