from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class MessageBox(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField(null=False, max_length=280)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "%s - %s" % (self.user.username, self.message)
    def display(self):
        self.date=timezone.now()
        self.save()

class Comments(models.Model):
    comment = models.TextField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    commented_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "%s - %s - " % (self.comment, self.user.username)
    def publish (self):
         self.commented_on = timezone.now()
         self.save()

class Like(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    dweet = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "%s" % self.user.username

    def publish(self):
        self.dweet = timezone.now()
        self.save()


#class Followers(models.Model):
   # user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
  #  followed_by = models.ManyToManyField(User,"self", related_name='follows', symmetrical=False)

# class Dweeter(models.Model):
#     user = models.ManyToManyField('self', symmetrical=False, through='Relationship')

class Relationship(models.Model):
    who = models.ForeignKey(User, related_name="who", on_delete=models.CASCADE)
    whom = models.ForeignKey(User, related_name="whom", on_delete=models.CASCADE)
    def __str__(self):
      return "%s - %s" % (self.who.username, self.whom.username)