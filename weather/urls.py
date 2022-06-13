from django.conf.urls import url
from django.urls import URLPattern
from weather import views

URLPatterns=[
    url(r'^$',views.Mainpage.as_view()),
]