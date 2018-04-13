from django.views.generic import TemplateView
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

from rest_auth.views import LogoutView

import json
import sys
import requests
from datetime import datetime


class HomeTemplateView(TemplateView):
    template_name = 'home.html'


class LoginView(APIView):
    def post(self, request):
        url = 'http://staging.tangent.tngnt.co/api-token-auth/'
        payload = {
            'username': request.data['username'],
            'password': request.data['password']
        }

        r = requests.post(url, payload)
        token = r.json()
        
        return Response(token)

class WhoAmI(APIView):
    def get(self, request, format=None):
        token = request.META.get('HTTP_AUTHORIZATION')
        url = 'http://staging.tangent.tngnt.co/api/employee/me/'
        r = requests.get(
            url, headers={
                'Authorization': 'Token {}'.format(token)
            })

        return Response(r.json())


class LogoutViewEx(LogoutView):
    authentication_classes = (authentication.TokenAuthentication, )


class EmployeeView(APIView):
    def get(self, request, format=None):
        token = request.META.get('HTTP_AUTHORIZATION')
        url = 'http://staging.tangent.tngnt.co/api/employee/'
        r = requests.get(
            url, headers={
                'Authorization': 'Token {}'.format(token)
            })

        return Response(r.json())


class FindAUnicornView(APIView):
    def get(self, request, format=None):
        token = request.META.get('HTTP_AUTHORIZATION')
        string = request.META.get('QUERY_STRING')
        url = 'http://staging.tangent.tngnt.co/api/employee/?' + string
        r = requests.get(
            url, headers={
                'Authorization': 'Token {}'.format(token)
            })

        return Response(r.json())


class CompanyStatsView(APIView):
    def get(self, request, format=None):
        token = request.META.get('HTTP_AUTHORIZATION')
        url = 'http://staging.tangent.tngnt.co/api/employee/'
        r = requests.get(
            url, headers={
                'Authorization': 'Token {}'.format(token)
            })

        employeeData = r.json()

        birthdaysThisMonth = self.birthday(employeeData)
        positionData = self.position(employeeData)
        companyDemographicData = self.demographics(employeeData)
        numberOfEmployees = self.numberEmployees(companyDemographicData)

        stats = {
            'Number_of_Employees': numberOfEmployees,
            'Birthdays_This_Month': birthdaysThisMonth,
            'Position_Data': positionData,
            'Company_Demographic_data': companyDemographicData,
        }

        print(stats, file=sys.stderr)
        return Response(stats)

    # data retrieval functions for class below

    def numberEmployees(self, companyDemographicData):
        sum_of = sum(companyDemographicData.values())
        return sum_of

    def birthday(self, employeeData):
        birthdayNames = []
        currentMonth = datetime.now().month

        for key in employeeData:
            birthMonth = int(key['birth_date'][5]) * 10 + int(
                key['birth_date'][6])
            if birthMonth == currentMonth:
                birthdayNames.append(
                    key['user']['first_name'] + ' ' + key['user']['last_name'])

        if not birthdayNames:
            birthdayNames.append(
                'No birthdays this month: Happy NOT birthday to everyone!')
        return birthdayNames

    def position(self, employeeData):
        uniqueList = []
        howMany = []
        for key in employeeData:
            if key['position']['name'] not in uniqueList:
                uniqueList.append(key['position']['name'])

        howMany = [0] * len(uniqueList)
        for x in range(0, len(uniqueList)):
            for key in employeeData:
                if uniqueList[x] == key['position']['name']:
                    howMany[x] = howMany[x] + 1

        positionDict = {}

        for x in range(0, len(uniqueList)):
            positionDict[uniqueList[x]] = howMany[x]

        return positionDict

    def demographics(self, employeeData):
        races = [0, 0, 0, 0, 0]  # black, coloured, indian, white, non-dominant
        raceChars = ['B', 'C', 'I', 'W', 'N']
        for key in employeeData:
            if key['race'] == 'B':
                races[0] = races[0] + 1
            elif key['race'] == 'C':
                races[1] = races[1] + 1
            elif key['race'] == 'I':
                races[2] = races[2] + 1
            elif key['race'] == 'W':
                races[3] = races[3] + 1
            elif key['race'] == 'N':
                races[4] = races[4] + 1

        raceDict = {}
        for x in range(0, len(races)):
            raceDict[raceChars[x]] = races[x]

        return raceDict
