from rest_framework import serializers

from modules.models import EducationModule


class ModulesSerializer(serializers.ModelSerializer):
    """Сериализатор для модели образовательного модуля."""
    class Meta:
        model = EducationModule
        fields = "__all__"
