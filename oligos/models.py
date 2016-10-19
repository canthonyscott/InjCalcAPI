from django.db import models

# Create your models here.

class Oligo(models.Model):
    gene = models.CharField(max_length=25)
    molecular_weight = models.IntegerField()
    owner = models.ForeignKey('auth.User', related_name='oligos')
    added_by = models.CharField(max_length=25)

    class Meta:
        ordering = ('gene',)


from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

# this code is triggered whenever a new user has been created and saved

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
