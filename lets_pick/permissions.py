# Code based from Code Institute's Django Rest Framework project
from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Returns True if the user wants to get the object or is the owner of
    the object
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Returns True if the user wants to get the object or is the author of
    the object
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
