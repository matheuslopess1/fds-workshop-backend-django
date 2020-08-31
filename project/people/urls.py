from django.urls import path
from .views import PersonListView, PersonDetailView


urlpatterns = [
    path('', PersonListView.as_view()),
    path('<int:pk>/', PersonDetailView.as_view())
]