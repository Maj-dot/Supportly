from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    
    else:
        form = UserCreationForm()
    return render(request, 'tickets/register.html', {'form': form})   

def home(request):
    return HttpResponse('<h1>Hello World!</h1>') 

@login_required
def ticket_list(request):
    return render(request,'ticket_list.html')