from django.urls import path, include
from . import views
from rest_framework import routers 

router = routers.DefaultRouter()
router.register('foods', views.FoodView)

router2 = routers.DefaultRouter()
router2.register('signup', views.SignView)


urlpatterns = [
    path('', include(router2.urls), name="index"),
    path('signup/', include(router2.urls), name ="signup")
]