from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    email = models.EmailField(unique = True)
    mobile = models.CharField(max_length = 15)
    password = models.CharField(max_length = 50)

    def __str__ (self) ->  str:
        return self.frist_name