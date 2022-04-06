from django.shortcuts import render, redirect

# Create your views here.
from core.forms import MessageForm


def index(request):
    form = MessageForm()
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, "core/index.html", {"form": form})

