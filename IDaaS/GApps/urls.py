from django.urls import path, include

from GApps.views import LoginView

urlpatterns = [
    path('login/', LoginView.as_view()),
]
