from rest_framework import permissions
from django.contrib.auth.models import Group
from rest_framework import permissions


def _is_in_group(user, group_name):
    """
    Takes a user and a group name, and returns `True` if the user is in that group.
    """
    try:
        return Group.objects.get(name=group_name).user_set.filter(id=user.id).exists()
    except Group.DoesNotExist:
        return None


def _has_group_permission(user, required_groups):
    return any([_is_in_group(user, group_name) for group_name in required_groups])


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        #print(obj.owner, request.user, "---------")
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.owner == request.user


class IsAdminGroup(permissions.BasePermission):
    """
    Special Permission Created to access content of "Admin Group"
    This checks if User is in Admin Group
    """
    required_groups = ['Admin Group']

    def has_permission(self, request, view):
        has_group_permission = _has_group_permission(
            request.user, self.required_groups)
        return request.user and has_group_permission

    def has_object_permission(self, request, view, obj):
        has_group_permission = _has_group_permission(
            request.user, self.required_groups)
        return request.user and has_group_permission


class IsAuthorGroup(permissions.BasePermission):
    """
    This permission is created so that members of Author group should be able to list,retrieve
    content, this checks run if request.user is not obj.owner, i.e if user requested is not owner
    of the content then he will be only allowed to list and filter content
    """
    required_groups = ['Author Group']

    def has_permission(self, request, view):
        has_group_permission = _has_group_permission(
            request.user, self.required_groups)
        return request.user and has_group_permission

    def has_object_permission(self, request, view, obj):
        has_group_permission = _has_group_permission(
            request.user, self.required_groups)
        return request.user and has_group_permission
