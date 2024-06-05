from django.db import models
from django.utils import timezone

# Create your models here.

# id (primary key - automático)
# first_name (string), last_name (string), phone (string)
# email (email), created_date (date), description (text)
#
# category (foreign key), show (boolean), owner (foreign key)
# picture (imagem)


class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=250, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
