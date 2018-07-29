from django.shortcuts import render

# Create your views here.



def index(req):
    template = 'webblog/index.html'
    context = {
        'sample':'This is the context information',
    }
    return render(req, template, context)