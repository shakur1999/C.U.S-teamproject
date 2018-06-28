from django.shortcuts import render, get_object_or_404, redirect
from .forms import cusform
from .models import cusapp

import math
import requests

# def homepage(request):
#     context = {
#
#     }
#     return render(request, 'index2.html', context)


def add_cusapp(request):
    if request.method == "POST":
        form = cusform(request.POST)
        if form.is_valid():
            cusapp_item = form.save(commit=False)
            cusapp_item.save()
            return redirect('/cusapp/' + str(cusapp.id) + '/')
    else:
        form = cusform()
    return render(request, 'cusapp/index.html', {'form': form})

def edit_cusapp(request, id=None):
    item = get_object_or_404(Blog, id=id)
    form = cusform(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return render(request, 'cusapp/index.html', {'form': form})


def cusapp(request, id=id):
    cusapp = cusapp.objects.get(id=id)
    return render(request, 'cusapp/index.html', {'cusapp': cusapp })

def maps(request):

    zip = '80301'
    response = requests.get(f'https://weather.cit.api.here.com/weather/1.0/report.json?product=observation&zipcode={zip}&oneobservation=true&app_id=DemoAppId01082013GAL&app_code=AJKnXv84fjrb0KIHawS0Tg')
    data = response.json()
    city = data['observations']['location'][0]['observation'][0]['city']
    state = data['observations']['location'][0]['observation'][0]['state']
    temperature = data['observations']['location'][0]['observation'][0]['temperature']
    latitude = data['observations']['location'][0]['latitude']
    longitude = data['observations']['location'][0]['longitude']
    fahrenheit = float(temperature) * 9/5+32
    f = math.ceil(fahrenheit)
    print(type(data))
    print(f'City: {city}, {state}' , '\n'
    f'Temperature: {f}''F'
    )
    print(f'Latitude: {latitude}', '\n'
    f'Longitude: {longitude}')

    context = {
        'city': city,
        'state': state,
        'temperature': f,
        'latitude': latitude,
        'longitude': longitude,
    }

    return render(request, 'cussapp/maps.html', context)

def loginReg(request):
    return render(request, 'cussapp/loginReg.html', {})

def form(request):
    return render(request, 'cussapp/form.html', {})