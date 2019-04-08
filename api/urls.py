from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'questions', QuestionViewSet, basename='question')

urlpatterns = router.urls