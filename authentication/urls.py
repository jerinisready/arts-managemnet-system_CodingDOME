from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include

from authentication.views import signup

urlpatterns = [

    path('signup/', signup, name="signup"),
    path('', include('django.contrib.auth.urls'))

]

