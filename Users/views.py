from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
# Create your views here.


def loginView(request):
    """ Vue de l'authentification (connexion de l'utilisateur) """
    error = ""
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username=username, password=password)#Vérification de l'authenticité de l'utilisateur

    if user is not None:
        login(request, user)
        return redirect("profile")
    else:
        error = "Nom d'utilisateur ou mot de passe incorrect"
    
    context = {
        'error': error,
    }
    return render(request, 'users/login.html', context)