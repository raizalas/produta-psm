#view function kirim email
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm

def contactView(request):
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data["subject"]
            from_email = form.cleaned_data["from_email"]
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ["raizal20ashari@apps.ipb.ac.id"])
                form = ContactForm()
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
    return render(request, "email.html", {"form": form})

def successView(request):
    return HttpResponse("Success! Thank you for your message.")