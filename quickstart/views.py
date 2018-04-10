from django.views.generic import TemplateView
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

from rest_auth.views import LogoutView

import json

class HomeTemplateView(TemplateView):
    template_name = 'home.html'

class LoginView(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    
    def post(self, request):
        url = 'http://staging.tangent.tngnt.co/api-token-auth/'
        payload = {'username':request.data.username,'password':request.data.password}
        r = requests.post(url, payload)
        token = r.json()
        
        #url = 'http://staging.tangent.tngnt.co/api/employee/me/'
        #r = requests.get(url,  headers={'Authorization': 'Token {}'.format(token['token'])})
        
        return HttpResponse(token)

class WhoAmI(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
     url = 'http://staging.tangent.tngnt.co/api/employee/me/'
     r = requests.get(url,  headers={'Authorization': 'Token {}'.format(token['token'])})
     return Response(r.json())
 
    

class LogoutViewEx(LogoutView):
    authentication_classes = (authentication.TokenAuthentication,)
    