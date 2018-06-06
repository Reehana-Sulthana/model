from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render
from dwitter.models import *
from django.contrib.auth.models import User


def Create_dweet():
 try:
     user = User.objects.get(username='kavi')
     dweet = MessageBox.objects.create(user=user, message="This is second message", date=timezone.now())
     print("dweet created")
     print(dweet)
     all_dweets = MessageBox.objects.all()
     print(all_dweets)
 except:
     print('user not found')

def Get_objects():
    try:
        dweeter = Like.objects.get(id=1)
        print(dweeter)
    except:
        print("object not exist")


def Delete_objects():
    try:
        instance = Like.objects.get(id=1)
        instance.delete()
        print("deleted")
        show = Like.objects.all()
        print(show)

    except Exception as exception:
        print("Exception : %s" % exception)


def Update_objects():
    try:
        updated_message= MessageBox.objects.filter(pk=2).update(message='Changed to new message')
        print(updated_message)
        print(MessageBox.objects.all())
    except Exception as exception:
        print("Exception: %s" % exception)


