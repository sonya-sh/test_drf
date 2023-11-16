from djoser.views import UserViewSet
from rest_framework import permissions

class IsAdminOrOnlyPost(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return request.user and request.user.is_staff
        return True

class CustomUserViewSet(UserViewSet):
    permission_classes = [IsAdminOrOnlyPost,]


