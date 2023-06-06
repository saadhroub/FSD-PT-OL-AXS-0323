from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse




def success(request):
    return HttpResponse("Form Done successfully")


def index(request):
    context={
        'tech': "Django"
            }
    return render(request, "index.html", context)

def sign_up(request):
    context = {
        'class': 'Django',
        'academy':'AXSOS ACademy'
    }
    return render(request, "form.html",context)



def form_process(request):
    # write you code here
    print(request.POST)
    return redirect("/success")


def another_method(request):
    return redirect("/redirected_route")


def redirected_method(request):
    return JsonResponse({"response": "JSON response from redirected_method", "status": True})