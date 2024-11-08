from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.http import HttpResponse


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("Phone or password is incorrect")  
    
    return render(request, 'login.html')