from django.shortcuts import render
import datetime
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from patient.models import *
from django.core import serializers
from django import forms

@csrf_exempt
def incoming_data(request):

    data = "";
    if request.method == 'POST':
        data += request.body
        json_data = json.loads(data)
        print type(json_data)
        print json_data["name"]
        try:
            print("till here")
            user = User.objects.create(name = json_data["name"],
                        is_male = json_data["gender"],
                        ethnicity = json_data["ethnicity"],
                        type_cancer = json_data["cancer type"],
                        expectancy = json_data["expectancy"],
                        treatment = json_data["treatment"],
                        email = json_data["email"])
            print(user)
            user.save()
            return HttpResponse({"200": "message_ok"}, content_type='application/json')
        except Exception as e:
            print e
            return e
    return HttpResponse(500)


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

def get_similar_patients(request,user_id):
    similar = []
    user = get_user_list(user_id)
    mutations = Genetic_info.objects.filter(users=user)
    for m in mutations:
        similar += m.users.all()
    data = serializers.serialize("json", similar)
    return HttpResponse(data, content_type='application/json')

def get_mutation_patients(request, chromosome, pos):
    all_mutations = Genetic_info.objects.get(pos = pos,chr = chromosome)
    data = serializers.serialize("json", all_mutations.users.all())
    return HttpResponse(data, content_type='application/json')

# def get_single_events(request,user_id):
#     user = User.objects.filter(pk=user_id)
#     data = serializers.serialize("json", user)
#     return HttpResponse(data, content_type='application/json')
