from rest_framework import permissions


class AdminOnlyView(permissions.BasePermission):
    """
    Custom permission to only allow Admin users to view Landlords.
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        # Check if the user has the role of "Admin"
        return request.user.role == "ADMIN"
