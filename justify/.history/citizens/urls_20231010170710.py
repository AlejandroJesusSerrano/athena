from django.urls import path
from .views import CitizenList, CitizenDetail, ProvinceList, ProvinceDetail

urlpatterns = [
  path('citizens/', CitizenList.as_view(), name='citizen-list'),
  path('citizens/<int:pk>', CitizenDetail.as_view(), name='citizen-detail'),

  path('province/', ProvinceList.as_view(), name='province-list'),
  path('province/<int:pk>', ProvinceDetail.as_view(), name='province-detail'),
]