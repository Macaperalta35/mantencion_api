# Commit 3: ViewSets implementados


from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Empresa, Equipo, Tecnico, PlanMantencion, OrdenTrabajo
from .serializers import (
    EmpresaSerializer,
    EquipoSerializer,
    TecnicoSerializer,
    PlanMantencionSerializer,
    OrdenTrabajoSerializer
)
from .permissions import ReadOnlyForUnauthenticated


# ----------------------------
# VIEWSETS PARA CADA ENTIDAD
# ----------------------------

class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    permission_classes = [ReadOnlyForUnauthenticated]


class EquipoViewSet(viewsets.ModelViewSet):
    queryset = Equipo.objects.all()
    serializer_class = EquipoSerializer
    permission_classes = [ReadOnlyForUnauthenticated]


class TecnicoViewSet(viewsets.ModelViewSet):
    queryset = Tecnico.objects.all()
    serializer_class = TecnicoSerializer
    permission_classes = [ReadOnlyForUnauthenticated]


class PlanViewSet(viewsets.ModelViewSet):
    queryset = PlanMantencion.objects.all()
    serializer_class = PlanMantencionSerializer
    permission_classes = [ReadOnlyForUnauthenticated]


class OrdenTrabajoViewSet(viewsets.ModelViewSet):
    queryset = OrdenTrabajo.objects.all()
    serializer_class = OrdenTrabajoSerializer
    permission_classes = [ReadOnlyForUnauthenticated]


# ----------------------------
# ENDPOINT DE PRUEBA
# ----------------------------

@api_view(["GET"])
def api_status(request):
    return Response({"status": "API funcionando correctamente"})
