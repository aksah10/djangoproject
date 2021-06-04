from django.shortcuts import render, HttpResponse

def index(request):
    context={
        'variable':"this is sent from index"
    }
    return render(request,'index.html', context)


def about(request):
    return render(request,'about.html')


def physics(request):
    return render(request,'physics.html')


def  chemistry(request):
         return render(request,'chemistry.html')


def maths(request):
     return render(request,'maths.html')         

def  biology(request):
     return render(request,'biology.html')


def contactus(request):
     return render(request,'contactus.html')
