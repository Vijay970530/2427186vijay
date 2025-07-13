from django.http import HttpResponse
from django.template import loader

def home(request):
    temp=loader.get_template('index.html')
    return HttpResponse(temp.render())