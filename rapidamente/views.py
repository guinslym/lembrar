from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView

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

def ShortUrlCreateVieww(request):
    return HttpResponse('<h1>Sjhow all the shuggies for this box: Only admin can view the suggies</h1>')

#success url
class ShortUrlDetailView(DetailView):
    template_name = 'shorturl_detail.html'
    model = ShortUrl

    def get_context_data(self, **kwargs):
            context = super(ShortUrlDetailView, self).get_context_data(**kwargs)
            context['now'] = timezone.now()
            return context

#redirectView

#About Us
