from django.shortcuts import redirect, render
from .models import Note
from django.contrib.auth import authenticate, login, logout
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# @login_required
def index(request):
    notes = Note.objects.all()
    context = {"Notes":notes}
    return render(request, 'index.html', context)
    # return HttpResponse("Hello, world. You're at the polls index.")

# @login_required
def noteCreate(request):
    if request.method == "POST":
        author = request.user
        title = request.POST.get("title")
        content = request.POST.get("content")
        createNote = Note.objects.create(author=author, title=title, content=content)
        createNote.save()
        return render(request, "noteCreate.html")
    else:
        notes = Note.objects.all()
        context = {"Notes": notes}
        return render(request, "noteCreate.html", context)

def signup(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        createNote = Note.objects.create(title=title, content=content)
        createNote.save()
    else:
        notes = Note.objects.all()
    context = {"Notes": notes}
    return render(request, "login.html", context)

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("pwd")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            notes = Note.objects.all()
            context = {"Notes": notes}
            return render(request, "index.html", context)
    else:
        
        return render(request, "login.html")

def logout_view(request):
    logout(request)
    return render(request, "login.html")
