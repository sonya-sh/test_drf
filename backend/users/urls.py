from django.urls import path, re_path, include
from .views import *

urlpatterns = [
    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),

    #path('auth/users/', CustomUserViewSet.as_view({'get': 'list', 'post': 'create'}), name='user-list'),
]
