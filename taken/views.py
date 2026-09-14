from django.shortcuts import render
from .models import Taak

def takenlijst(request):
    taken = Taak.objects.all()
    return render(request, 'taken/takenlijst.html', {'taken': taken})

# Create your views here.
