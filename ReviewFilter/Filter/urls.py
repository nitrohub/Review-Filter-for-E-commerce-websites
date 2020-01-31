from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$',index,name='index'),
    url(r'^display_review$',display_review,name='display_review')

]