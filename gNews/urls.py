from django.urls import path, include
from rest_framework import routers

from gNews import views



router = routers.DefaultRouter()
# router.register(r'problems', views.ProblemsViewset)
# router.register(r'tags', views.TagViewSet)


urlpatterns = [ 
    path('gnews/search/', views.search),
    path('gnews/headlines/', views.headlines)
]