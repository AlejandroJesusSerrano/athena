from django.urlsa import path
from .views import CitizenList, CitizenDetail

urlpatterns = [
  path('citizens/', CiitizenList.as_view(), name='citizen-list'),
  path('citizens/<int:pk>', CitizenDetail.as_view(), name='citizen-detail'),
]