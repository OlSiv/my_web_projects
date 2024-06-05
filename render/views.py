from django.shortcuts import render
from .models import Message
from django.contrib.auth.models import User 


def index(request):

    mess_m = Message.objects.all()[::-1]
    print(mess_m[0].id)



    users_names = User.objects.all()

    context = {
        'mess1': mess_m, 
        'users_names': users_names,

               }
###
    return render(request, 'render/index.html', 
                  context=context
                  )


