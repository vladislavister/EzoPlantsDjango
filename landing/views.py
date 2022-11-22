from django.shortcuts import render
import datetime

def landing(request):
    name = "vladislavister"
    return render(request, 'landing/landing.html', locals())