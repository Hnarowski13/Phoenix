from django.conf.urls import url

from cooks import views

urlpatterns = [
    url(r'^', views.cooks, name='phoenix-cooks'),
]