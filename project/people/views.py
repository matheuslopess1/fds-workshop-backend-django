from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Person


class PersonListView(ListView):
    model = Person


class PersonDetailView(DetailView):
    model = Person


class PersonCreateView(CreateView):
    model = Person
    fields = '__all__'


class PersonUpdateView(UpdateView):
    model = Person
    fields = '__all__'
