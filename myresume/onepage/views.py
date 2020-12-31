from django.shortcuts import render
from onepage.forms import NewUserForm
import pandas
# Create your views here.

def index(request):
    form = NewUserForm()
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return render(request, 'onepage/index.html', {'form': form})
        else:
            form = NewUserForm()

    return render(request, 'onepage/index.html', {'form': form})
