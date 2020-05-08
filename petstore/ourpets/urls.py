from django.urls import path
from . import views

app_name = 'ourpets'

urlpatterns = [
    # Все животные
    path('', views.AnimalsListView.as_view(), name='animal_list'),
    path('<slug:animal>/', views.BreedListView.as_view(), name='breed_list'),
    path('<int:pk>/<slug:breed>/', views.PetListView.as_view(), name='pet_list'),
    path('detail/<int:pk>', views.PetDetailView.as_view(),name='pet_detail')
]