from django.shortcuts import render 

from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class Home(APIView):
    '''
        Base test
    '''

    def get(self,request,*args,**kwargs):
        return Response("Hello world")
