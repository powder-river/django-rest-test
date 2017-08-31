from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from ldap.ldap import DukeLdap
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
# @csrf_exempt
class SearchLdap(APIView):
    def get(request,format=None):
        ldap =  DukeLdap()
        response = ldap.search()

        return Response(response)

    def post(self, request):
        return Response({"response":[{"my-key":"my-value"}]})

    def delete(self,request):
        return (Response({"response":[{"my-key":"my-value"}]}))