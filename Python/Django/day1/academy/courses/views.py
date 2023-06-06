from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse



def success(request):
    return render(request, "success.html")


def index(request):
    context={
        'tech': "Django"
            }
    return render(request, "index.html", context)



def sign_up(request):
    return render(request, "form.html")


def form_process(request):
    request.session['name'] = request.POST['name']
    request.session['email'] = request.POST['email']
    return redirect("/success")


