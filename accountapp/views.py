from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from accountapp.models import HelloWorld


def hello_world(request):
    if request.method == 'POST':

        get = request.POST.get('hello_world')
        new_hello_world = HelloWorld()
        new_hello_world.text = get
        new_hello_world.save()

        return HttpResponseRedirect(reverse('accountapp:hello_world'))
    else:
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list': HelloWorld.objects.all()})