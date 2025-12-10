# Commit 3: Serializers implementados


from rest_framework import serializers
from .models import Empresa, Equipo, Tecnico, PlanMantencion, OrdenTrabajo


class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = "__all__"


class EquipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipo
        fields = "__all__"


class TecnicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tecnico
        fields = "__all__"


class PlanMantencionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanMantencion
        fields = "__all__"


class OrdenTrabajoSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdenTrabajo
        fields = "__all__"
