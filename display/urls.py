from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import NoticeViewset


router = DefaultRouter()
router.register('', NoticeViewset, basename='Notice')


urlpatterns = [
    path('',views.dept ),
    path('off', views.off ),
    path('notices/',include(router.urls))
]