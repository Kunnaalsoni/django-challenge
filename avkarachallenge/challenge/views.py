from django.shortcuts import render
from challenge.models import Features
# Create your views here.
def home(request):
    data = Features.objects.all()
    return render(request, 'index.html', {'data':data})