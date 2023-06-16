from django.shortcuts import render, HttpResponse,redirect
from .models import User
from django.contrib import messages
import bcrypt

def index(request):
    return render(request, "index.html")

def register(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()  
        print(pw_hash)
        request.session['username'] = fname + " "+ lname
        request.session['status']="Registered"
        User.objects.create(first_name=fname, last_name=lname,email=email, password=pw_hash)
    return redirect("/success")

def login(request):
    errors2 = User.objects.login_validator(request.POST)
    if len(errors2) > 0:
        for key, value in errors2.items():
            messages.error(request, value)
        return redirect('/')

    users = User.objects.filter(email=request.POST['email2'])
    if users:
        logged_user = users[0]
        if bcrypt.checkpw(request.POST['password2'].encode(), logged_user.password.encode()):
            request.session['username'] = logged_user.first_name
            request.session['status']="logged in"
            return redirect('/success')
        print("""Wrong password""")
    return redirect("/")

def success(request):
    # if request.method== "GET":
    #     return redirect('/')
    context={
        'username': request.session['username'],
        'status':request.session['status'],
    }
    return render(request,"success.html",context)

def logout(request):
    del request.session['username']
    del request.session['status']
   # request.session.flush()
    return redirect('/')
