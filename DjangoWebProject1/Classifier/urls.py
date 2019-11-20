
from Classifier.views import Train, Predict
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path

app_name = 'Classifier'

urlpatterns = [
    path(r'^train/$', Train.as_view(), name="train"),
    path(r'^predict/$', Predict.as_view(), name="predict"),
]