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

#setting a predefine unique SLUG in the session
#request.session['fav_color'] = 'blue'
#http://stackoverflow.com/a/25521706/2581266

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

def hello(request):
    #   import ipdb; ipdb.set_trace()
    return HttpResponse('<h1>hello</h1>')
#redirectView

#About Us
def handler404(request):
    pathinfo = request.path_info
    if len(pathinfo)<2:
        if pathinfo == '/':
            #Go fill a form to create a urlshortened
            return redirect('http://localhost:8004/hello/')
        else:
            response = redirect('/')
            response.status_code = 301
            return response
    pathinfo = request.path_info[1::]
    website = ShortUrl.objects.filter(slug=pathinfo)
    if website:
        response =  redirect(website[0].url)
        response.status_code = 301
        return response
    else:
        #I didn't found the url
        response = render(request, 'page_not_found.html')
        response.status_code = 404
        return response


def handler500(request):
    response = render(request, 'emplois/server_error.html')
    response.status_code = 500
    return response
