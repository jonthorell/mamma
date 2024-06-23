from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class index(TemplateView):
    '''Class used to display the index page '''

    template_name = 'core/index.html'
    
class grief(TemplateView):
    '''Class used to display the grief page '''

    template_name = 'core/grief.html'
    
class gone(TemplateView):
    '''Class used to display the gone page '''

    template_name = 'core/gone.html'