from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    EmpresaViewSet,
    EquipoViewSet,
    TecnicoViewSet,
    PlanViewSet,
    OrdenTrabajoViewSet,
    api_status
)

router = DefaultRouter()
router.register("companies", EmpresaViewSet)
router.register("equipments", EquipoViewSet)
router.register("technicians", TecnicoViewSet)
router.register("plans", PlanViewSet)
router.register("workorders", OrdenTrabajoViewSet)

urlpatterns = [
    path("status/", api_status),
    path("", include(router.urls)),
]
