from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return bool(
            request.method in permissions.SAFE_METHODS or
            request.user and
            request.user
            and request.user.is_authenticated
            and request.user.is_staff
        )


class FavoritePermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return bool(obj.owner == request.user)