from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from .models import TodoData
from .serializers import TodoSerializer
from .pagination import TodoPagination

class TodoDataList(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request: Request, **kwargs) -> Response:
        todo = TodoData.objects.filter(user=request.user).order_by('-date')
        paginator = TodoPagination()
        todo_items = paginator.paginate_queryset(todo, request)
        serializer = TodoSerializer(todo_items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request: Request, **kwargs) -> Response:
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class TodoDataDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk: int) -> TodoData:
        try:
            return TodoData.objects.get(pk=pk)
        except TodoData.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, _: Request, pk: int) -> Response:
        todo = self.get_object(pk)
        serializer = TodoSerializer(todo)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request: Request, pk: int) -> Response:
        todo = self.get_object(pk)
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request: Request, pk: int) -> Response:
        todo = self.get_object(pk)
        serializer = TodoSerializer(todo, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, _: Request, pk: int) -> Response:
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)