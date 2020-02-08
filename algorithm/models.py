from datetime import timedelta, date

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.contrib.auth.models import User

from algorithm.algorithm import interval


class Card(models.Model):
    front = models.CharField(max_length=255)
    back = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Practice(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    next_practice = models.DateField(auto_now_add=True)
    times_practiced = models.PositiveIntegerField(default=1)
    easy_factor = models.FloatField(default=2.5)

    class Meta:
        ordering = ['next_practice']

    def set_next_practice(self, rating):
        days, ef = interval(self.times_practiced, rating, self.easy_factor)
        self.next_practice = date.today() + timedelta(days=days)
        self.times_practiced += 1
        self.easy_factor = ef

    def delay(self):
        self.next_practice = date.today() + timedelta(days=1)
