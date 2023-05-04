# from django.views.generic import View
# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PersonsSerialize
from .models import Person
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class Home(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser, ]

    def get(self, request):
        persons = Person.objects.all()
        ser_data = PersonsSerialize(instance=persons, many=True)

        return Response(data=ser_data.data)

    def post(self, request):
        name = request.data['name']
        return Response({'name': name})
