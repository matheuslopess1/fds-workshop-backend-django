from django.test import TestCase, Client
from django.http import HttpResponsePermanentRedirect
from .models import Person


class PersonTest(TestCase):
    def test_route_list(self):
        """deve retornar 200 na rota /people/"""
        request = Client()
        response = request.get('/people/')
        self.assertEqual(response.status_code, 200)

    def test_route_detail(self):
        """deve retornar 200 na rota /people/<int:pk>/"""
        person = Person(first_name='any_first_name', last_name='any_last_name')
        person.save()
        request = Client()
        response = request.get('/people/{}/'.format(person.id))
        self.assertEqual(response.status_code, 200)

    def test_route_create_get(self):
        """deve retornar 200 na rota /people/create/"""
        request = Client()
        response = request.get('/people/create/')
        self.assertEqual(response.status_code, 200)

    def test_route_create_post(self):
        """deve retornar 302 na rota /people/create/ com o método POST"""
        request = Client()
        response = request.post('/people/create/', {'first_name': 'any_first_name', 'last_name': 'any_last_name'})
        people = Person.objects.all()
        self.assertEqual(len(people), 1)
        person = people[0]
        self.assertRedirects(response, '/people/{}/'.format(person.id), status_code=302)
