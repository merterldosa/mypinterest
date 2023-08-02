from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from accountapp.models import HelloWorld
from django.views.generic import CreateView
from django.contrib.auth.models import User


def hello_world(request):
    if request.method == 'POST':

        get = request.POST.get('hello_world')
        new_hello_world = HelloWorld()
        new_hello_world.text = get
        new_hello_world.save()

        return HttpResponseRedirect(reverse('accountapp:hello_world'))
    else:
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list': HelloWorld.objects.all()})

class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/create.html'