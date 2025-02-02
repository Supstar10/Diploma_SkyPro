from rest_framework import viewsets

from modules.models import EducationModule
from modules.serializers import ModulesSerializer


class ModulesViewSet(viewsets.ModelViewSet):
    """
    Представление для управления образовательными модулями.
    Реализует CRUD операции модуля.
    """
    serializer_class = ModulesSerializer
    queryset = EducationModule.objects.all()
