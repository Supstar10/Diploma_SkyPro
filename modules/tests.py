from rest_framework.test import APITestCase
from rest_framework import status
from modules.models import EducationModule
from modules.serializers import ModulesSerializer


class ModulesViewSetTest(APITestCase):
    def setUp(self):
        # Создаем тестовые данные
        self.module1 = EducationModule.objects.create(
            order=1,
            title="Модуль 1",
            description="Описание модуля 1",
            is_published=True
        )
        self.module2 = EducationModule.objects.create(
            order=2,
            title="Модуль 2",
            description="Описание модуля 2",
            is_published=False
        )

    def test_list_modules(self):
        """Проверяем получение списка модулей."""
        url = "/modules/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Должны быть два модуля

    def test_create_module(self):
        """Проверяем создание нового модуля через API."""
        url = "/modules/"
        data = {
            "order": 3,
            "title": "Новый модуль",
            "description": "Описание нового модуля",
            "is_published": True
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(EducationModule.objects.count(), 3)

    def test_update_module(self):
        """Проверяем обновление существующего модуля."""
        url = f"/modules/{self.module1.id}/"
        data = {
            "order": 1,
            "title": "Обновленный модуль",
            "description": "Обновленное описание",
            "is_published": False
        }
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.module1.refresh_from_db()
        self.assertEqual(self.module1.title, "Обновленный модуль")
        self.assertFalse(self.module1.is_published)

    def test_partial_update_module(self):
        """Проверяем частичное обновление модуля."""
        url = f"/modules/{self.module1.id}/"
        data = {
            "title": "Частично обновленный модуль"
        }
        response = self.client.patch(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.module1.refresh_from_db()
        self.assertEqual(self.module1.title, "Частично обновленный модуль")

    def test_delete_module(self):
        """Проверяем удаление модуля."""
        url = f"/modules/{self.module1.id}/"
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(EducationModule.objects.count(), 1)


class ModulesSerializerTest(APITestCase):
    def setUp(self):
        # Создаем тестовый объект EducationModule
        self.module = EducationModule.objects.create(
            order=1,
            title="Тестовый модуль",
            description="Это описание тестового модуля",
            is_published=True
        )

    def test_serializer_valid_data(self):
        """Проверяем, что сериализатор корректно обрабатывает валидные данные."""
        data = {
            "order": 2,
            "title": "Новый модуль",
            "description": "Описание нового модуля",
            "is_published": False
        }
        serializer = ModulesSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data["order"], 2)
        self.assertEqual(serializer.validated_data["title"], "Новый модуль")
        self.assertEqual(serializer.validated_data["description"], "Описание нового модуля")
        self.assertFalse(serializer.validated_data["is_published"])

    def test_serializer_invalid_data(self):
        """Проверяем, что сериализатор корректно обрабатывает невалидные данные."""
        invalid_data = {
            "order": -1,  # Неверное значение для положительного целого числа
            "title": "",  # Пустое название
            "description": "Описание нового модуля"
        }
        serializer = ModulesSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("order", serializer.errors)
        self.assertIn("title", serializer.errors)

    def test_serializer_fields(self):
        """Проверяем, что все поля сериализатора соответствуют ожиданиям."""
        serializer = ModulesSerializer(instance=self.module)
        data = serializer.data
        self.assertEqual(set(data.keys()), {"id", "order", "title", "description", "is_published"})
