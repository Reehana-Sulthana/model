from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class MessageBox(models.Model):
    User_id = models.ForeignKey(User, on_delete=models.CASCADE)
    Message = models.TextField(null=False, max_length=280)
    Date = models.DateTimeField(default=timezone.now)

class Comments(models.Model):
    comment = models.TextField(null=True)
    comment_id = models.ForeignKey(User, on_delete=models.CASCADE)
    commented_on = models.DateTimeField(default=timezone.now)

class Like(models.Model):
    like_id = models.ForeignKey(User,on_delete=models.CASCADE)
    liked_on=models.DateTimeField(default=timezone.now)


class Followers(models.Model):
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    followed_by = models.ManyToManyField("self", related_name='follows', symmetrical=False)



