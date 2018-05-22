from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def signup(request):
    if request.method == 'POST': #User has info and ready to signup
        if request.POST['password1'] == request.POST['password2']: #checks if pwd match
            try:
                user = User.objects.get(username=request.POST['username']) #checks if username already exist
                return render(request, 'accounts/signup.html', {'error': 'Username already taken'}) #message when it already exist
            except User.DoesNotExist: #if user doesnt exist and pwd match
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1']) #creates new user
                auth.login(request, user) #logs new user in
                return redirect('home') #redirects them to homepage
        else:
            return render(request, 'accounts/signup.html', {'error': 'Password must match'}) #when pwd dont match
    else:
        return render(request, 'accounts/signup.html')# if user isnt ready to create an account
    
        
def login(request):
    return render(request, 'accounts/login.html')


def logout(request):
    #logout needs to goto the homepage
    return render(request, 'accounts/signup.html')
