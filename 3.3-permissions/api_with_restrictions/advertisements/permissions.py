from rest_framework.permissions import BasePermission

class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        current_user = str(request.user)
        # т.к. юзернеймы уникальные, а имя суперюзера - admin,
        # то имя текущего пользователя проверяется на admin
        if current_user == 'admin':
            return True
        return request.user == obj.creator
