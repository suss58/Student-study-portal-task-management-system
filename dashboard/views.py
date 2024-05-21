from django.shortcuts import redirect, render
from .forms import *
from .forms import NotesForm
from django.contrib import messages
from .models import Homework, Notes
from django.views import generic

def home(request):
    return render(request, 'dashboard/home.html')

def notes(request):
    if request.method == 'POST':
        form = NotesForm(request.POST)
        if form.is_valid():
            notes = Notes(
                user=request.user,
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description']
            )
            notes.save()
            messages.success(request, f"Notes added by {request.user.username} successfully")
            return redirect('notes')
        else:
            messages.error(request, "Failed to add note. Please check the form for errors.")
    else:
        form = NotesForm()

    notes = Notes.objects.filter(user=request.user)
    context = {'notes': notes, 'form': form}
    return render(request, 'dashboard/notes.html', context)

def delete_note(request, pk=None):
    Notes.objects.get(id=pk).delete()
    return redirect("notes")

class NotesDetailView(generic.DetailView):
    model = Notes

def homework(request):
    if request.method == 'POST':
        form = HomeworkForm(request.POST)
        if form.is_valid():
            try:
                finished = request.POST.get('is_finished', 'off') == 'on'
            except KeyError:
                finished = False
            

            homeworks=Homework(
                user=request.user,
                subject=request.POST['subject'],
                title=request.POST['title'],
                description=request.POST['description'],
                due=request.POST['due'],
                is_finished=finished
            )
            homeworks.save()
            messages.success(request, f"Homeworks added by {request.user.username} successfully")
            return redirect('homework')
        else:
            messages.error(request, "Failed to add homeworks. Please check the form for errors.")
    else:
        form = HomeworkForm()
            
    
    homework = Homework.objects.filter(user=request.user)
    homework_done = len(homework) == 0

    context = {
        'homeworks': homework,
        'homework_done': homework_done,
        'form': form,
    }
    return render(request, 'dashboard/homework.html', context)


def update_homework(request,pk=None):
    homework=Homework.objects.get(id=pk)
    if homework.is_finished== True:
        homework.is_finished=False
    else:
        homework.is_finished=True
    homework.save()
    return redirect('homework')