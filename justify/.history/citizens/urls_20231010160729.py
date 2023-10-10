from django.urls import path
from .views import CitizenList, CitizenDetail

urlpatterns = [
  path('citizens/', CitizenList.as_view(), name='citizen-list'),
  path('citizens/<int:pk>', CitizenDetail.as_view(), name='citizen-detail'),
]