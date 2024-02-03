from django.shortcuts import render, get_object_or_404,redirect
from .models import Note

# Create your views here.
def note_list(request):
    notes = Note.objects.all()
    return render(request,'notes/note_list.html',{'notes':notes})

def note_delete(request, id):
    note = get_object_or_404(Note, id=id)
    if request.method == 'POST':
        note.delete()
        return redirect('note_list')
    else:
        return render(request, 'notes/note_confirm_delete.html', {'note': note})