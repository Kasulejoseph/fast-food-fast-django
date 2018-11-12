from django.urls import path, include
from . import views
from rest_framework import routers 

router = routers.DefaultRouter()
router.register('foods', views.FoodView)
router.register('signup', views.SignView)


urlpatterns = [
    path('', include(router.urls), name="index")
]