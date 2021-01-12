from django.urls import path
from .views import *


urlpatterns =[
    path('', index, name='home'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('email', email, name='email'),
    path('gallery', gallery, name='gallery'),
    path('blog', blog, name='blog'),
    path('comment', comment, name='comment'),

]


