from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import http
import base64


def index(request):
    return HttpResponse("Tu będzie planer:")

def a_label(request, latitude = 0.0, longitude = 0.0):
    userpass = "a722a820-b0c1-47fb-9167-565331c3cf8e:29871d98df36fb8d045e03468894214740a3c81dc2a4447a7d3d259ac7e2304ed122c67a2513c07c71c8d1b14568aacdfaa47b5cfbef7b396ba48473ffaa3fc34f8b3ac579297fa98288be2097d0bfb7a9b1b9262f412240178dfca8d8f5cb5323f0aac6c14b3d6295302f74fa21d013"
    authString = base64.b64encode(userpass.encode()).decode()
    conn = http.client.HTTPSConnection("api.astronomyapi.com")

    headers = { 'Authorization': "Basic YTcyMmE4MjAtYjBjMS00N2ZiLTkxNjctNTY1MzMxYzNjZjhlOjI5ODcxZDk4ZGYzNmZiOGQwNDVlMDM0Njg4OTQyMTQ3NDBhM2M4MWRjMmE0NDQ3YTdkM2QyNTlhYzdlMjMwNGVkMTIyYzY3YTI1MTNjMDdjNzFjOGQxYjE0NTY4YWFjZGZhYTQ3YjVjZmJlZjdiMzk2YmE0ODQ3M2ZmYWEzZmMzNGY4YjNhYzU3OTI5N2ZhOTgyODhiZTIwOTdkMGJmYjdhOWIxYjkyNjJmNDEyMjQwMTc4ZGZjYThkOGY1Y2I1MzIzZjBhYWM2YzE0YjNkNjI5NTMwMmY3NGZhMjFkMDEz" }

    conn.request("GET", "/api/v2/bodies/positions?longitude=%s&latitude=%s&elevation=1&from_date=2024-01-08&to_date=2024-01-08&time=17%3A46%3A41" %longitude %latitude, headers=headers)

    res = conn.getresponse()
    data = res.read()

    

    return HttpResponse(data.decode("utf-8"))