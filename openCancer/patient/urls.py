from django.conf.urls import url
from patient import views

urlpatterns = [
    url(r'^(?P<user_id>\d+)/$', views.get_single_user, name='get_single_user'),
    url(r'^(?P<user_id>\d+)/mutations$', views.get_single_user_mutations, name='get_single_user_mutations'),
    url(r'^(?P<user_id>\d+)/events$', views.get_single_user_events, name='get_single_user_events'),
    url(r'^$', views.get_all_patients, name='get_all_patient'),
]