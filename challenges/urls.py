from django.urls import path

from . import views

urlpatterns = [
    path("", views.list_months, name="list-months"),
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge, name="month-challenge"),

]