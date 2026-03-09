from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from tasks.views import RegisterAPIView
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='task-list')),
    path('admin/', admin.site.urls),
    path('api/', include('tasks.urls')),
    
    # Auth
    path('api/auth/register/', RegisterAPIView.as_view(), name="register"),
    path('api/auth/login/', TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name="token_refresh")
]
