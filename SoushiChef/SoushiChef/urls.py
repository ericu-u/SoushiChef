from django.contrib import admin
from django.urls import path

# Pages
from landing.views import landing
from cook.views import cook, route_cook
from login.views import login
from signup.views import signup
from menu.views import menu

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing, name="landing"),
    path('cook', cook, name="cook"),
    path('login', login, name="login"),
    path('signup', signup, name="signup"),
    path('menu', menu, name="menu"),
    path('post/ajax/route_cook', route_cook, name="route_cook")
]
