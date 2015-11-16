from django.conf.urls import url

from finance import views

urlpatterns = [
    url(r'^', views.finance, name='phoenix-finance'),
]