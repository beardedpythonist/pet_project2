from rest_framework import permissions

# код взят с сайта официальной документации

class IsOwnerOrReadOnly(permissions.BasePermission):
      def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return obj.author == request.user
