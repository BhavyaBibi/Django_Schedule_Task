from django.urls import path
from weather import views
urlpatterns = [
    path('', views.MainPage.as_view()),
]
