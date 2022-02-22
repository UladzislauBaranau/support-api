from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsSupportOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return request.user.profile.is_support


class IsUserNotSupport(BasePermission):
    def has_permission(self, request, view):
        return not request.user.profile.is_support

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class IsSupportUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.profile.is_support

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
