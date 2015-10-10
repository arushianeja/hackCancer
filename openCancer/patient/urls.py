from django.conf.urls import url
from patient import views

urlpatterns = [
    url(r'^(?P<user_id>\d+)/$', views.get_single_user, name='get_single_user'),
    url(r'^$', views.get_all_patients, name='get_all_patient'),
]