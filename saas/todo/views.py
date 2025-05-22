from django.shortcuts import render

from todo.forms import UniversityForm

def myview(request):
    if request.method == "POST":
        pass
    else:
        form = UniversityForm()
        return render(request, 'todo/uform.html', {'form':form})