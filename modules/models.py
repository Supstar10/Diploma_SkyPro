from django.db import models


# Create your models here.
class EducationModule(models.Model):
    """
    Модель для образовательного модуля.
    Содержит информацию о порядке, названии и описании модуля.
    """

    order: int = models.PositiveIntegerField(verbose_name='Порядковый номер')
    title: str = models.CharField(max_length=255, verbose_name='Название')
    description: str = models.TextField(verbose_name='Описание')
    is_published: bool = models.BooleanField(default=False, verbose_name='Статус публикации')

    class Meta:
        verbose_name = 'Модуль'
        verbose_name_plural = 'Модули'
        ordering = ['order']

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта.
        """
        return self.title
