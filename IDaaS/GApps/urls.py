from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from GApps.views import LoginView
from GApps.views import ProfileView

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('logout/', auth_views.logout, {'next_page': '/accounts/login/'}, name='logout'),
    path('profile/', login_required(ProfileView.as_view()))
]
