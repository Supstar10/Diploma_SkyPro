from rest_framework import viewsets

from modules.models import EducationModule
from modules.serializers import ModulesSerializer


class ModulesViewSet(viewsets.ModelViewSet):
    serializer_class = ModulesSerializer
    queryset = EducationModule.objects.all()
