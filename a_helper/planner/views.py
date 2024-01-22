from tokenize import Number
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import http
import base64
from .models import *
from datetime import date


def index(request):
    
    return render(request, 'planner/index.html')

def planner_site(request, longitude = 0.0, latitude = 0.0, date = date.today()):
    object_list = A_object.objects
    planets_dict = {'mercury':'', 
                    'venus':'',
                    'mars':'',
                    'jupiter': '',
                    'saturn': '',
                    'uranus': '',
                    'neptune': '',
                    'pluto':''
                    }
    hour_list = ["22%3A00%3A00", "02%3A00%3A00", "06%3A00%3A00"]
    resources = planet_info(request, longitude, latitude, date, hour_list[0])

    return render(request, 'planner/planner.html', resources)


def planet_info(request, longitude, latitude, date, hour):
    
    planets_dict = {'mercury':'', 
                    'venus':'',
                    'mars':'',
                    'jupiter': '',
                    'saturn': '',
                    'uranus': '',
                    'neptune': ''
                    }
    key_list = list(planets_dict.keys())
    conn = http.client.HTTPSConnection("api.astronomyapi.com")

    headers = { 'Authorization': "Basic YTcyMmE4MjAtYjBjMS00N2ZiLTkxNjctNTY1MzMxYzNjZjhlOjI5ODcxZDk4ZGYzNmZiOGQwNDVlMDM0Njg4OTQyMTQ3NDBhM2M4MWRjMmE0NDQ3YTdkM2QyNTlhYzdlMjMwNGVkMTIyYzY3YTI1MTNjMDdjNzFjOGQxYjE0NTY4YWFjZGZhYTQ3YjVjZmJlZjdiMzk2YmE0ODQ3M2ZmYWEzZmMzNGY4YjNhYzU3OTI5N2ZhOTgyODhiZTIwOTdkMGJmYjdhOWIxYjkyNjJmNDEyMjQwMTc4ZGZjYThkOGY1Y2I1MzIzZjBhYWM2YzE0YjNkNjI5NTMwMmY3NGZhMjFkMDEz" }

    for planet in key_list:
        conn.request("GET", "/api/v2/bodies/positions/{0}?latitude={1}&longitude={2}&from_date={3}&to_date={3}&elevation=166&time=23%3A59%3A59".format(planet, longitude, latitude, date), headers=headers)
        res = conn.getresponse()
        planets_dict[planet] = res.read().decode("utf-8")
    
    return planets_dict

def DS_info(request, name, longitude, latitude, date, hour):
    conn = http.client.HTTPSConnection("api.astronomyapi.com")

    headers = { 'Authorization': "Basic YTcyMmE4MjAtYjBjMS00N2ZiLTkxNjctNTY1MzMxYzNjZjhlOjI5ODcxZDk4ZGYzNmZiOGQwNDVlMDM0Njg4OTQyMTQ3NDBhM2M4MWRjMmE0NDQ3YTdkM2QyNTlhYzdlMjMwNGVkMTIyYzY3YTI1MTNjMDdjNzFjOGQxYjE0NTY4YWFjZGZhYTQ3YjVjZmJlZjdiMzk2YmE0ODQ3M2ZmYWEzZmMzNGY4YjNhYzU3OTI5N2ZhOTgyODhiZTIwOTdkMGJmYjdhOWIxYjkyNjJmNDEyMjQwMTc4ZGZjYThkOGY1Y2I1MzIzZjBhYWM2YzE0YjNkNjI5NTMwMmY3NGZhMjFkMDEz" }
    conn.request("GET", "/api/v2/search?exact={0}&match_type=exact".format(name), headers=headers)
    res = conn.getresponse()

    return res.read().decode("utf-8")

