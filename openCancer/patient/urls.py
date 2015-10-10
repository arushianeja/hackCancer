from django.conf.urls import url
from patient import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]