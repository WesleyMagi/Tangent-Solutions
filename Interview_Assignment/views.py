from django.views.generic import TemplateView
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

from rest_auth.views import LogoutView

import json
import sys
import requests

class HomeTemplateView(TemplateView):
    template_name = 'home.html'

class LoginView(APIView):

    def post(self, request):
        url = 'http://staging.tangent.tngnt.co/api-token-auth/'
        payload = {'username':request.data['username'],'password':request.data['password']}

        r = requests.post(url, payload)
        token = r.json()

        print("Hello World", file=sys.stderr)

        #url = 'http://staging.tangent.tngnt.co/api/employee/me/'
        #r = requests.get(url,  headers={'Authorization': 'Token {}'.format(token['token'])})

        return Response(token)

class WhoAmI(APIView):
    def get(self, request, format=None):
     token = request.META.get('HTTP_AUTHORIZATION')
     url = 'http://staging.tangent.tngnt.co/api/employee/me/'
     r = requests.get(url,  headers={'Authorization': 'Token {}'.format(token)})
     
     #print(r.json(), file=sys.stderr)
     
     return Response(r.json())



class LogoutViewEx(LogoutView):
    authentication_classes = (authentication.TokenAuthentication,)

class EmployeeView(APIView):
    def get(self, request, format=None):
     token = request.META.get('HTTP_AUTHORIZATION')
     url = 'http://staging.tangent.tngnt.co/api/employee/'
     r = requests.get(url,  headers={'Authorization': 'Token {}'.format(token)})
     
     #print(r.json(), file=sys.stderr)
     
     return Response(r.json())
 
class FindAFriendView(APIView):
    def get(self, request, format=None):
     token = request.META.get('HTTP_AUTHORIZATION')
     url = 'http://staging.tangent.tngnt.co/api/employee/'
     r = requests.get(url,  headers={'Authorization': 'Token {}'.format(token)})
     
     #print(r.json(), file=sys.stderr)
     
     return Response(r.json())

class CompanyStatsView(APIView):
    def get(self, request, format=None):
     token = request.META.get('HTTP_AUTHORIZATION')
     url = 'http://staging.tangent.tngnt.co/api/employee/'
     r = requests.get(url,  headers={'Authorization': 'Token {}'.format(token)})

     #print(r.json(), file=sys.stderr)     
     return Response(r.json())
 