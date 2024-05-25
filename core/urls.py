from django.urls import path

from . import views

urlpatterns = [
    path("", views.index.as_view(), name="index"),
    path("grief", views.grief.as_view(),name="grief")
]