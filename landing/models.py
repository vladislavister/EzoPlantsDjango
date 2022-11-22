from django.db import models

class User(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField()

    def __str__(self):
        return "%s %s" % (self.id, self.email)