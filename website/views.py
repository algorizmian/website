from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from .models import Project
from .forms import ContactForm


def home(request):
    # projects = Project.objects.all()
    # context = {'projects': projects}
    return render(request, 'website/home.html')


def our_work(request):
    return render(request, 'website/ourwork.html')


def about(request):
    context = {}
    return render(request, 'website/about.html', context)


def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, email, ['layla0911@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, 'website/contact.html', {'form': form})