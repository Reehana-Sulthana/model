from django.conf.urls import url


from . import views

urlpatterns = [
    url(r'^$', views.Hello, name='hello'),
    url(r'^like/(?P<id>\d+)/$', views.Get_objects, name='like'),
    url(r'^delete/(?P<id>\d+)/$', views.Delete_objects, name='delete'),

]
