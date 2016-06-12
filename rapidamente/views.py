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


def homepage_and_create_shorturl(request, slug=None):
    '''
    This is the homepage
    and
    it will have a Form to create box
    then it will show the Sharelink
    '''
    if request.method == 'POST':
        # A form was POSTED

        #import ipdb; ipdb.set_trace()
        shorturl_form = ShortUrlForm(data=request.POST)
        #Valid ?
        if shorturl_form.is_valid():
            #Create the Box
            new_shorturl = shorturl_form.save()
            messages.add_message(request, messages.INFO, 'Congrats!!!')
            return render(  request,'shorturl_detail.html',
                            {'object': new_shorturl} )
        else:
            messages.add_message(request, messages.INFO, 'Please fill the form')
    form = ShortUrlForm()
    return render( request,
                  'shorturl_form.html', {'form':form }
                )
def detail_box(request, slug):
    '''

    '''
    short_url = get_object_or_404(ShortUrl, slug=slug)
    return render( request, 'shorturl_detail.html', {'object':short_url} )

#redirectView

#About Us
