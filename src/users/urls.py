from django.urls import path

from . import views


app_name="users"
urlpatterns = [
    path("signin/", views.SignInView.as_view(), name="signin"),
    path("signup/", views.signup, name="signup"),
    path("signout/", views.SignoutView.as_view(), name="signout"),
    path("mypage/", views.MypageView.as_view(), name="mypage"),
]