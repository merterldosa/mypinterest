from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from accountapp.models import HelloWorld


def hello_world(request):
    if request.method == 'POST':

        get = request.POST.get('hello_world')
        new_hello_world = HelloWorld()
        new_hello_world.text = get
        new_hello_world.save()

        return render(request, 'accountapp/hello_world.html', context={'new_hello_world' : new_hello_world.text})
    else:
        return render(request, 'accountapp/hello_world.html', context={'text': 'GET REQUEST'})