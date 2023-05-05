# from django.views.generic import View
# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PersonsSerialize, QuestionSerializer
from .models import Person, Answer, Question
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status


class Home(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser, ]

    def get(self, request):
        persons = Person.objects.all()
        ser_data = PersonsSerialize(instance=persons, many=True)

        return Response(data=ser_data.data)

    def post(self, request):
        name = request.data['name']
        return Response({'name': name})


class QuestionsView(APIView):
    def get(self, request):
        questions = Question.objects.all()
        srz_data = QuestionSerializer(instance=questions, many=True).data
        return Response(srz_data, status=status.HTTP_200_OK)

    def post(self, request):
        srz_data = QuestionSerializer(data=request.data)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data, status=status.HTTP_201_CREATED)
        return Response(srz_data.errors, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        questions = Question.objects.get(pk=pk)
        srz_data = QuestionSerializer(instance=questions, data=request.data, partial=True)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data, status=status.HTTP_200_OK)
        return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        questions = Question.objects.get(pk=pk)
        questions.delete()
        return Response({'message': 'questions delete'}, status=status.HTTP_200_OK)

