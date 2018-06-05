from django.shortcuts import render

# Create your views here.


def create_dweet(request):
    user_id = 123
    dweet = MessageBox.create()
    dweet.save()
