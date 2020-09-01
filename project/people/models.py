from django.db import models
from django.urls import reverse


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def get_absolute_url(self):
        return reverse('people_person_detail_view', kwargs={'pk': self.pk})
