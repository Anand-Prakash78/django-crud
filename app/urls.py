from django.urls import path,include
from . import views

urlpatterns = [
path('',views.app,name='app'),
path('insertpage/',views.insertpage,name='insertpage'),
path('insertNewsPage/',views.insertNewsPage ,name='insertNewsPage'),
path('inserNews/',views.inserNews,name='inserNews'),
path('showNews/',views.showNews,name='shownews'),
path('descriptionNews/<title>',views.descriptionNews,name='descriptionNews'),

path('insert/',views.insert,name='insert'),
path('showpage/',views.showpage,name='showpage'),
path('editpage/<int:pk>',views.editpage,name='editpage'),
path('deletedata/<int:pk>:',views.deletedata,name='deletedata'),
path('update/<int:pk>:',views.update,name='update'),

path('sendOtp',views.sendOtp,name='sendOtp'),



]