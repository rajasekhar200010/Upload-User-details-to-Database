from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from .models import speakerinfo
# Create your views here.

def home(request):
    all_details = speakerinfo.objects.all()
    count =speakerinfo.objects.all().count()
    context=count
    return render(request, "pages/index.html",{'all_details': all_details, 'context':context})

def listspeakers(request):
    all_details = speakerinfo.objects.all()
    count =speakerinfo.objects.all().count()
    context=count
    return render(request, "pages/listspeakers.html",{'all_details': all_details, 'context':context})

def adduser(request):

    if request.method=='POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        phnumber =request.POST['phnumber']

        myuser = User.objects.create_user(username, fname,  email)

        myuser.save()

        speakerInfo = speakerinfo(username=username, fname= fname, lname= lname, email=email, phnumber =phnumber)

        speakerInfo.save()

        messages.success(request,"speaker was added")

        return redirect('adduser')





    return render(request, "pages/adduser.html")


def removeuser(request, id):
    all_details = speakerinfo.objects.all()
    count =speakerinfo.objects.all().count()
    context=count

    delete = speakerinfo.objects.get(id=id)
    delete.delete()
    #return render(request, "pages/listspeakers.html",{'all_details': all_details, 'context':context})
    return HttpResponseRedirect("/listspeakers")

#def removeuser(request):
#    return render(request, "pages/removeuser.html")