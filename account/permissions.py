from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import BasePermission


class IsSchoolUser(BasePermission):
    def has_permission(self, request, view):
        if request.auth["user_type"] == "school":
            return True
        raise PermissionDenied
