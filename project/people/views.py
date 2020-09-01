from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
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


class PersonDeleteView(DeleteView):
    model = Person
    success_url = reverse_lazy('people_person_list_view')
