from django.urls import path, include
from . import views

# myurlpatterns

urlpatterns = [

    path('', views.testdata, name='Covid19 url'),

]
