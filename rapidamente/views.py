from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages

#Contact form
from django.views.generic.edit import FormView
#Box, Suggestion
from .models import ShortUrl
from .forms import ShortUrlForm

#Create View

#About Us
