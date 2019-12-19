from django.shortcuts import render
from .models import Contact


def home(request):
    if request.method == 'POST':
        email = request.POST.get('email1')
        message = request.POST.get('message1')
        obj = Contact()
        obj.email = email
        obj.message = message
        obj.save()
    return render(request, template_name='index.html')


