from rest_framework.permissions import BasePermission, SAFE_METHODS

class ReadOnlyForUnauthenticated(BasePermission):
    """
    Usuarios NO autenticados: solo lectura (GET).
    Usuarios autenticados: pueden crear, editar y eliminar registros.
    """
    def has_permission(self, request, view):
        # Si el método es seguro (GET, HEAD, OPTIONS), permitir siempre
        if request.method in SAFE_METHODS:
            return True
        
        # Para POST/PUT/PATCH/DELETE → solo usuarios autenticados
        return request.user and request.user.is_authenticated
