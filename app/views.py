from django.shortcuts import render
from ast import Is
from calendar import month
from cmath import nan
from ipaddress import ip_address
from turtle import color
from urllib import request
from django.shortcuts import render
from numpy import longlong
from rest_framework.views import APIView
from django.views.generic import TemplateView
from ipware import get_client_ip
from rest_framework.response import Response
from rest_framework import status
from .models import apirates
import datetime
from django.utils import timezone
import requests
import json
import folium
import pandas as pd

# Create your views here.


def testdata(request):

    return render(request, 'chart.html')
