from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile."""

    def has_object_permission(self, request, view, obj):
        """Check if user is trying to update his own profile"""

        if request.method in permissions.SAFE_METHODS: #Ako method e vo SAFE_METHODS, primer GET a ne e PATCH/PUT/DELETE
            return True

        return obj.id == request.user.id #Ako ID na objektot sto saka da napravi izmena e isto so IDto na avtenticiraniot korisnik

class PostOwnStatus(permissions.BasePermission):
    """Allows users to update their own status"""

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id
