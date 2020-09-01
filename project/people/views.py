from django.views.generic import ListView, DetailView, CreateView
from .models import Person


class PersonListView(ListView):
    model = Person


class PersonDetailView(DetailView):
    model = Person


class PersonCreateView(CreateView):
    model = Person
    fields = '__all__'
