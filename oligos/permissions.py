from rest_framework import permissions
from django.contrib.auth.models import User

class IsOwnerOrNothing(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        return obj.owner == request.user


class IsStaffOrTargetUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return view.action == 'retrieve' or request.user.is_staff

    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or obj == request.user

