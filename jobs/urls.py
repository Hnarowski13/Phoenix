from django.conf.urls import url

from jobs import views

urlpatterns = [
    #(r'^', views.jobs),
    url(r'^', views.jobs, name='phoenix-jobs'),
]