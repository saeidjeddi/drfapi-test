from rest_framework import serializers


class PersonsSerialize(serializers.Serializer):
    name = serializers.CharField(max_length=35)
    age = serializers.IntegerField()
    email = serializers.EmailField() 
