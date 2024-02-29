from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ThreadViewSet, MessageViewSet, get_messages_by_thread_id

router = DefaultRouter()
router.register(r'threads', ThreadViewSet)
router.register(r'messages', MessageViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('threads/<int:thread_id>/messages/', get_messages_by_thread_id, name='get_messages_by_thread_id'),

]
