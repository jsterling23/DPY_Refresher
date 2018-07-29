from django.shortcuts import render
from ..prac_models.models import *

# Create your views here.


def index(req):
    template = 'prac_models/index.html'
    context = {
        'people':Person.objects.all(),
        'groups':Group.objects.all(),
        'membership':Membership.objects.all(),
    }
    return render(req, template, context)