from django.shortcuts import render
#
from .models import Message


def index(request):
    #
    mess = Message.objects.all()
    return render(request, 'render/index.html', {'mess': mess})
