from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Bug
from .forms import BugForm

# Create your views here.
def index(request):
    return render(request, 'home.html')

def register_bug(request):
    if request.method == 'POST':
        form = BugForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bug_list')  
    else:
        form = BugForm()
    return render(request, 'register_bug.html', {'form': form})

def view_bug(request, bug_id):
    bug = Bug.objects.get(id=bug_id)
    return render(request, 'view_bug.html', {'bug': bug})

def bug_list(request):
    bugs = Bug.objects.all()
    return render(request, 'bug_list.html', {'bugs': bugs})