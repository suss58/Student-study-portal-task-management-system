from django.shortcuts import redirect, render
from .forms import *
from .forms import NotesForm
from django.contrib import messages
from .models import Notes

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