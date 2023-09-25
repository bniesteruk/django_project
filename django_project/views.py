from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import MyDataSerializer


class MyDataView(APIView):
    def get(self, request):
        # Logika obsługi zapytania GET
        # Przykład: Pobierz dane z bazy danych
        data = SomeModel.objects.all()
        serializer = MyDataSerializer(data, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        #Logika obsługi zapytania POST
        # Przykład: Zapisz dane do bazy danych
        serializer = MyDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
