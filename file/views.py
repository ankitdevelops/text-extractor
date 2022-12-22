from django.shortcuts import render, redirect
from .forms import *
from .models import Text


def home(request):
    form = TextForm()
    if request.method == "POST":
        form = TextForm(request.POST, request.FILES)
        if form.is_valid():
            form_data = form.save(commit=False)
            form_data.user = request.user
            form_data.save()
            return redirect("home")

    user_data = Text.objects.all().filter(user=request.user).order_by("-created")
    context = {"form": form, "user_data": user_data}

    return render(request, "home.html", context)


def details(request, id):
    text = Text.objects.get(id=id)
    context = {"text": text}
    return render(request, "details.html", context)
