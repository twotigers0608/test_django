from django.conf.urls import url
from . import views

urlpatterns = {
    url(r'test/$', views.Home.as_view()),
    url(r'show/$', views.Show.as_view()),
}