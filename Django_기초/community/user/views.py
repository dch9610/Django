from django.shortcuts import render

# Create your views here.
def register(request):
    if request.method == "GET":
        return render(request, 'register.html')

    elif request.method == "POST":
        return render(request, 'register.html')