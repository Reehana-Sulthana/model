from django.http import HttpResponse
from django.shortcuts import render
from dwitter.models import *
from django.contrib.auth.models import User


def Create_dweet():
   user = User.objects.get(username='reehana')
   dweet = MessageBox.objects.create(user=user, message="This is second message", date=timezone.now())
   print("dweet created")
   print(dweet)
   all_dweets = MessageBox.objects.all()
   print(all_dweets)

def Get_objects():
    obj = Like.objects.get(pk=2)
    print(obj)

def Delete_objects():
    instance = Like.objects.get(id=2)
    instance.delete()
    print("deleted")
    show = Like.objects.all()
    print(show)

def Update_objects():
   updated_message= MessageBox.objects.filter(pk=1).update(message='updated')
   print(updated_message)
   print(MessageBox.objects.all())

