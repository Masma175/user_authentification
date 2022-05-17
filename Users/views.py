from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth import authenticate, login
# Create your views here.

def dashboard(request):
    """ Home View """
    return HttpResponse("<h1>Ceci est Votre Dashboard</h1>")


def loginView(request):
    """ Vue de l'authentification (connexion de l'utilisateur) """
    error = ""
    if request.method == "POST":

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)#Vérification de l'authenticité de l'utilisateur

        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            error = "Nom d'utilisateur ou mot de passe incorrect"
    
    context = {
        'error': error,
    }
    return render(request, 'users/login.html', context)