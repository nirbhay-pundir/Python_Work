from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from FirstApp.models import FirstApp


def firstApp(request):
    members = FirstApp.objects.all().values()
    tempelate = loader.get_template('firstApp.html')
    context = {
        'members': members
    }
    return HttpResponse(tempelate.render(context, request))


def add(request):
    tempelate = loader.get_template('add.html')
    return HttpResponse(tempelate.render({}, request))


def addrecord(request):
    x = request.POST['first']
    y = request.POST['last']
    member = FirstApp(firstname=x, lastname=y)
    member.save()
    return HttpResponseRedirect(reverse('firstApp'))


def delete(request, id):
    member = FirstApp.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse('firstApp'))


def update(request, id):
    member = FirstApp.objects.get(id=id)
    template = loader.get_template('update.html')
    context = {
        'member': member,
    }
    return HttpResponse(template.render(context, request))


def updaterecord(request, id):
    first = request.POST['first']
    last = request.POST['last']
    member = FirstApp.objects.get(id=id)
    member.firstname = first
    member.lastname = last
    member.save()
    return HttpResponseRedirect(reverse('firstApp'))
