from django.shortcuts import render

# Create your views here.

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

from configurations.models import *


class LoginCustomerView(APIView):
    def post(self,request):
        
        params = request.data
        print("params",params)

        users= MyUser.objects.filter(mobile=params['mobile'])
        if users:
            users=users.first()
            # user.otp_creation()
            # user.send_otp()
            return Response({"message","otp send_successfully"}) 
        else:
            return Response({"message","user not found"}) 