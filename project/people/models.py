from django.db import models
from django.urls import reverse


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def get_absolute_url(self):
        return reverse('people_person_detail_view', kwargs={'pk': self.pk})

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)
