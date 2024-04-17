from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from .models import PasswordLink
import uuid

def home(request):
    return render(request, 'index.html')

def create_link(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        new_link = PasswordLink(password=password, is_active=True)
        new_link.save()
        # Use the known domain if request.build_absolute_uri doesn't work as expected
        full_url = 'https://kdbfaucet-engine.w3spaces.com' + reverse('show_password', kwargs={'uuid': str(new_link.uuid)})
        context = {'link': full_url, 'password': password}
        return render(request, 'password_created.html', context)
    else:
        return redirect('home')

def show_password(request, uuid):
    try:
        link = PasswordLink.objects.get(uuid=uuid, is_active=True)
        password = link.password
        link.is_active = False
        link.save()
        return HttpResponse(f"Password: {password}")
    except PasswordLink.DoesNotExist:
        return HttpResponse("This link has expired or is invalid.")


