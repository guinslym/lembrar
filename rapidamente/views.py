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
class ShortUrlCreateView(CreateView):
    model = ShortUrl
    fields = ['url', 'nickname']
    template_name = 'shorturl_form.html'

#About Us
