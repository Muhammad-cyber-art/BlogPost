from django.urls import path
from .views import signup_view
from django.contrib.auth.views import LogoutView
from .views import logout_view

urlpatterns = [
    path('signup/',signup_view,name='signup'),
    path("logout/", LogoutView.as_view(next_page="home"), name="logout"),
    path('logout/',logout_view,name='logout')
]
