from django.views.generic import TemplateView
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response

import json
import requests

class HomeTemplateView(TemplateView):
    template_name = 'home.html'

class LoginView(APIView):

    def post(self, request):
     url = 'http://staging.tangent.tngnt.co/api-token-auth/'
     payload = {'username':request.data['username'], 'password':request.data['password']}
     r = requests.post(url, payload)
     token = r.json()
        
     if(token['token']):
      return Response(token)

class WhoAmI(APIView):
    def get(self, request, format=None):
     url = 'http://staging.tangent.tngnt.co/api-token-auth/'
     payload = {'username':request.data['username'], 'password':request.data['password']}
     r = requests.post(url, payload)
     token = r.json()   
     #url = 'http://staging.tangent.tngnt.co/api/employee/me/'
     #r = requests.get(url,  headers={'Authorization': 'Token {}'.format(token['token'])})
     if(token['token']):
      return Response(r.json())
