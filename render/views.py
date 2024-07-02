from django.shortcuts import render
from .models import Message
from django.contrib.auth.models import User 
from django.http import HttpResponse


def index(request):

#     mess_m = Message.objects.all()[::-1]
#     users_names = User.objects.all()

#     context = {
#         'mess1': mess_m, 
#         'users_names': users_names,

#                }
# ###
#     return render(request, 'render/index.html', 
#                   context=context
#                   )

    return HttpResponse('Hello') 

