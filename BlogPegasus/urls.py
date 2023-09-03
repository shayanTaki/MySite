from django.urls import path
from . import views
urlpatterns = [

    path("", views.index, name="BlogPegasus"),
    path("e", views.nav, name="BlogPegasus"),
    path("HakingMusic", views.HakingMusic, name="BlogPegasus"),

]

