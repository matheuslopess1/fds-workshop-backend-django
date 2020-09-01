from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.http import Http404
from .models import Person


def person_list_view(request):
    people = Person.objects.all()
    return render(request, 'people/person_list.html', { 'object_list': people })


def person_detail_view(request, pk):
    try:
        person = Person.objects.get(pk=pk)
        return render(request, 'people/person_detail.html', {'object': person})
    except Person.DoesNotExist:
        raise Http404('Pessoa não encontrada')


class PersonCreateView(CreateView):
    model = Person
    fields = '__all__'


class PersonUpdateView(UpdateView):
    model = Person
    fields = '__all__'


class PersonDeleteView(DeleteView):
    model = Person
    success_url = reverse_lazy('people_person_list_view')
