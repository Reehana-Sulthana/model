
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from dwitter.models import *
from django.contrib.auth.models import User
from .models import Like
import logging
logger = logging.getLogger('dwitter')

def Create_dweet():
 logger.info("coming from create_object function....")
 try:
     user = User.objects.get(username='kavi')
     dweet = MessageBox.objects.create(user=user, message="This is second message", date=timezone.now())
     print("dweet created")
     print(dweet)
     all_dweets = MessageBox.objects.all()
     print(all_dweets)
 except:
     logger.exception('user not found')


def Get_objects(request,id):
      logger.info("from get_objects function return all")
      try:
        like = Like.objects.get(id=id)
        like_dict = {
            "id": like.id,
          #  "user": Like.user_id.User.username,
            "date": like.dweet
        }
        return JsonResponse(like_dict)
      except Exception as exception:
          logger.exception("Exception: %s" % exception)


def Delete_objects(request,id):
    logger.info("from Delete_object function")
    try:
        instance = Like.objects.get(id=id)
        instance.delete()
        show = Like.objects.all()
        return HttpResponse(instance,show)
    except Exception as exception:
        logger.exception("Exception : %s" % exception)


def Update_objects():
    logger.info("from update_objects function")
    try:
        updated_message= MessageBox.objects.filter(pk=2).update(message='Changed to new message')
        print(updated_message)
        print(MessageBox.objects.all())
    except Exception as exception:
        logger.exception("Exception: %s" % exception)


def Hello(request):
    return HttpResponse("hello")


