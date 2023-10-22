
from django.urls import path

from app import views

urlpatterns = [
    # path("app/",include(("app.urls","app"),namespace="app")),
    path("index/",views.index),
    path("register/",views.register),
    path("login/",views.login),
    path("home/",views.home),
    path("addstudent/",views.addstudent),
    path("delstu/",views.delstu),
    path("bindstu/",views.bindstu),
    path("quit/",views.quit),
    # path("index/",views.index),
]

