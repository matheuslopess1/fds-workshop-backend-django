from django.views.generic import ListView, DetailView
from .models import Person


class PersonListView(ListView):
    model = Person


class PersonDetailView(DetailView):
    model = Person
