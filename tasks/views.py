from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer, RegisterSerializer
from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from django.conf import settings
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework import permissions, status
from .permissions import IsOwner

class TaskViewSet(viewsets.ModelViewSet):
    # queryset = Task.objects.all().order_by('-created_at')
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    
    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user).order_by('-created_at')
    
    # Guardar la tarea con el usuario authenticado
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        
    def get_object(self):
        obj = get_object_or_404(self.get_queryset(), pk=self.kwargs.get('pk'))
        return obj
    
    @action(detail=False, methods=['get'])
    def completed(self, request):
        queryset = self.get_queryset().filter(completed=True)
        page = self.paginate_queryset(queryset)
        serializer = TaskSerializer(page, many=True)
        return self.get_paginated_response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def not_completed(self, request):
        queryset = self.get_queryset().filter(completed=False)
        page = self.paginate_queryset(queryset)
        serializer = TaskSerializer(page, many=True)
        return self.get_paginated_response(serializer.data)


class RegisterAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "id": user.id,
                "username": user.username,
                "email": user.email
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['POST'])
# @permission_classes([permissions.AllowAny])
# def register(request):
#     serializer = RegisterSerializer(data=request.data)
#     if serializer.is_valid():
#         user = serializer.save()
#         return Response({
#             'id': user.id, 
#             'username': user.username,
#             'email': user.email
#         }, status=status.HTTP_201_CREATED)
    
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class TaskListCreateAPIView(APIView):
    
#     def get(self, request):
#         queryset = Task.objects.all().order_by('-created_at')
#         completed = request.query_params.get('completed') #/tasks?completed=true
#         if completed in ('true', 'false'):
#             queryset = queryset.filter(completed=(completed=="true"))
        
#         paginator = PageNumberPagination()
#         paginator.page_size = settings.REST_FRAMEWORK['PAGE_SIZE']
#         page = paginator.paginate_queryset(queryset, request)
        
#         serializer = TaskSerializer(page, many=True)
#         return paginator.get_paginated_response(serializer.data)
        
#     def post(self, request):
#         serializer = TaskSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class TaskRetrieveUpdateDeleteAPIView(APIView):
    
#     def get_object(self, pk):
#         return get_object_or_404(Task, pk=pk)
    
#     def get(self, request, pk):
#         task = self.get_object(pk)
#         serializer = TaskSerializer(task)
#         return Response(serializer.data)
    
#     def put(self, request, pk):
#         task = self.get_object(pk)
#         serializer = TaskSerializer(task, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def patch(self, request, pk):
#         task = self.get_object(pk)
#         serializer = TaskSerializer(task, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)    
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, pk):
#         task = self.get_object(pk)
#         task.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    