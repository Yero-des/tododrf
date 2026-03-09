from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer
from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from django.conf import settings

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-created_at')
    serializer_class = TaskSerializer

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
    