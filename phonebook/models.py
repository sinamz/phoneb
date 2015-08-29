from django.db import models as m


class Contact(m.Model):
    name = m.CharField(max_length=30)
    number = m.IntegerField()
    email = m.EmailField()

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name