from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.shortcuts import get_object_or_404, render, redirect
from .models import *

def IndexView(request):
    main_pics = Main_Picture.objects.all()
    social_media_btns = Social_Media_btn.objects.all()
    formations = Formation.objects.all().order_by('end_year')
    certificates = Certificate.objects.all()
    return render(request, 'core/index.html',
        {'social_media_btns': social_media_btns,
         'main_pics': main_pics,
         'formations': formations,
         'certificates': certificates,
        }
    )

def BioView(request):
    bio_pictures = Bio_Picture.objects.all()
    return render(request, 'core/Pages/biography.html',
        {'bio_pictures': bio_pictures}
    )

