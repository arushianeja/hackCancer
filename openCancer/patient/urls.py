from django.conf.urls import url
from patient import views

urlpatterns = [
    url(r'^$', views.get_all_users, name='get_all_users'),
]