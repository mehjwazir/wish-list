from django.db import models

# Create your models here.


class Wish(models.Model):
    description = models.TextField(max_length=300)

    def __str__(self):
        return f'{self.description}'
