from django.shortcuts import render
import datetime
import json
from django.http import HttpResponse
from patient.models import User
from django.core import serializers

# def current_datetime(request):
#     now = datetime.datetime.now()
#     html = "<html><body>It is now %s.</body></html>" % now
#     return HttpResponse(html)

def index(request):
    users = User.objects.all()
    data = serializers.serialize("json", users)
    return HttpResponse(data, content_type='application/json')