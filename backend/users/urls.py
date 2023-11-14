from django.urls import path, re_path, include
from .views import *

urlpatterns = [
    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]

"""
http://0.0.0.0:8001/users_api/auth/token/login/     POST

Запрос
{
"password": "string",
"username": "string"
}

Ответ
{
    "auth_token": "723b76186bfe8c9e4e04efcb06fdf57b59e6f21c"
}
"""
