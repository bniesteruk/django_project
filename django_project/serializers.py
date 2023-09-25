from rest_framework import serializers

class MyDataSerializer(serializers.Serializer):
    field1 = serializers.CharField()
    field2 = serializers.IntegerField()