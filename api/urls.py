from django.urls import path

from . import views

urlpatterns = [
  path('explosion/blast_calc/', views.BlastRetrieveView.as_view(), name='api_blast_calc'),
]