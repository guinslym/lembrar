from django import forms
from . models import  ShortUrl
from django.forms import ModelForm

class ContactForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass

class ShortUrlForm(ModelForm):
    class Meta:
        model = ShortUrl
        fields = ['url']
    '''
    def clean_nickname(self):
        nickname = self.cleaned_data['nickname']
        if ShortUrl.objects.filter(nickname=nickname).exists():
            raise forms.ValidationError("This nickname is already exists")
        return nickname
    '''
