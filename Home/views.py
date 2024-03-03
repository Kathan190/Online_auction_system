from django.shortcuts import render, HttpResponse
from Home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        description = request.POST.get("description")
        contact = Contact(name=name, email=email, subject=subject, description=description)
        contact.save()
        messages.success(request, "Your message have been sent succesfully")
    return render(request, "index.html")
