from modules.apps import ModulesConfig
from rest_framework.routers import DefaultRouter

from modules.views import ModulesViewSet

app_name = ModulesConfig.name

router = DefaultRouter()
router.register(r"modules", ModulesViewSet, basename="modules")

urlpatterns = [

] + router.urls
