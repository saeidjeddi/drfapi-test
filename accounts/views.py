from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import UserRegisterSerializers


class UserRegisterView(APIView):
    def post(self, request):
        ser_data = UserRegisterSerializers(data=request.POST)
        if ser_data.is_valid():
            ser_data.create(ser_data.validated_data)

            return Response(ser_data.data)
        return Response(ser_data.errors)
