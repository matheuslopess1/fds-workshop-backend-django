from django.urls import path
from .views import PersonListView, PersonDetailView, PersonCreateView, PersonUpdateView


urlpatterns = [
    path('', PersonListView.as_view(), name='people_person_list_view'),
    path('<int:pk>/', PersonDetailView.as_view(), name='people_person_detail_view'),
    path('create/', PersonCreateView.as_view(), name='people_person_create_view'),
    path('<int:pk>/update', PersonUpdateView.as_view(), name='people_person_update_view')
]