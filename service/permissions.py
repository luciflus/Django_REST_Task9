from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAuthorPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(
            request.method in SAFE_METHODS or
            request.user and request.user.is_authenticated and
            obj.profile == request.user.profile and
            obj.profile.is_sender == True)

class IsPassengerPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
