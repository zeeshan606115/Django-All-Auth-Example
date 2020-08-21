from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
import pprint
# Create your views here.


@login_required
def test(request):
    pprint.pprint(request.user)
    return HttpResponse("It is working user: "+str(request.user))