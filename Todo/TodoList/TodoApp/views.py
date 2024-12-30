from django.shortcuts import render, redirect
from .models import *


# Create your views here.
def home(request):
    projets=Projet.objects.all( )
    return render(request,"home.html", context={"projets":projets})

def CreateProject(request):
    if request.method == "POST":
       titre = request.POST.get('titre')
       description = request.POST.get('description')
       date_echeance = request.POST.get('date_echeance')
       Projet.objects.create(titre=titre,description=description,date_echeance=date_echeance)
       
       return redirect('home')

    return render(request , 'CreateProject.html')


def CreateTaches(request):
    projets = Projet.objects.all()
    if request.method == "POST":
       titre = request.POST.get('titre')
       description = request.POST.get('description')
       date_echeance = request.POST.get('date_echeance')
       completed = request.POST.get('completed')
       projet = request.POST.get('projet')
       Projet.objects.get(id=projet)
       Taches.objects.create(titre=titre,description=description,date_echeance=date_echeance,completed=completed,projet=projet)
       
       return redirect('home')

    return render(request , 'CreateTaches.html', context= {"projets":projets})


def updateTaches(request, id):
    tache = Taches.objects.get(id=id)
    if request.method == "POST":
       tache.titre = request.POST.get('titre')
       tache.description = request.POST.get('description')
       tache.date_echeance = request.POST.get('date_echeance')
       tache.completed = request.POST.get('completed')
       tache.projet = Projet.objects.get(id=request.POST.get('projet'))
       tache.save()
       
       return redirect('home')

    return render(request , 'updateTaches.html', context={"tache":tache})

def deleteTaches(request, id):
    tache = Taches.objects.get(id=id)
    tache.delete()
    return redirect('home')

def updateProject(request, id):
    projet = Projet.objects.get(id=id)
    if request.method == "POST":
       projet.titre = request.POST.get('titre')
       projet.description = request.POST.get('description')
       projet.date_echeance = request.POST.get('date_echeance')
       projet.save()
       
       return redirect('home')

    return render(request , 'updateProject.html', context={"projet":projet})

def deleteProject(request, id):
    projet = Projet.objects.get(id=id)
    projet.delete()
    return redirect('home')

def detailProject(request, id):
    projet = Projet.objects.get(id=id)
    taches = Taches.objects.filter(projet=projet)
    return render(request , 'detailProject.html', context={"projet":projet, "taches":taches})