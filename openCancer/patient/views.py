from django.shortcuts import render
import datetime
import json
from django.http import HttpResponse
from patient.models import *
from django.core import serializers

# def current_datetime(request):
#     now = datetime.datetime.now()
#     html = "<html><body>It is now %s.</body></html>" % now
#     return HttpResponse(html)

def get_all_patients(request):
    users = User.objects.filter(is_patient=1)
    data = serializers.serialize("json", users)
    return HttpResponse(data, content_type='application/json')

def get_all_doctors(request):
    users = User.objects.filter(is_patient=0)
    data = serializers.serialize("json", users)
    return HttpResponse(data, content_type='application/json')

def get_single_user(request,user_id):
    user = User.objects.filter(pk=user_id)
    data = serializers.serialize("json", user)
    return HttpResponse(data, content_type='application/json')
 
def get_user_list(id):
    user = User.objects.filter(pk=id)
    data = Genetic_info.objects.filter(users__in=user)
    return data

def get_single_user_mutations(request,user_id):
    data = get_user_list(user_id)
    data = serializers.serialize("json", data)
    return HttpResponse(data, content_type='application/json')
 
# def get_single_user_events(request,user_id):
#     user = User.objects.filter(pk=user_id)
#     data = serializers.serialize("json", user)
#     return HttpResponse(data, content_type='application/json')
# 
# def get_single_events(request,user_id):
#     user = User.objects.filter(pk=user_id)
#     data = serializers.serialize("json", user)
#     return HttpResponse(data, content_type='application/json')