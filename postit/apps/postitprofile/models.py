from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PostitProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	follows = models.ManyToManyField('self', related_name = "followed_by", symmetrical = False)

User.postitprofile = property(lambda u:PostitProfile.objects.get_or_create(user=u)[0])