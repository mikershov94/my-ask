from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'questions', QuestionViewSet, basename='question')
router.register(r'popular', PopularViewSet, basename='popular')

urlpatterns = router.urls