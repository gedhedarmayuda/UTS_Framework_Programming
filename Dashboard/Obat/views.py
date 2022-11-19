from django.shortcuts import render
from .models import *
# Create your views here.
def obat_list(request):
    Obats = Obat.objects.all()
    
    obats = {
        "obats":Obats,
    }
    return render(request, "obat/list_obat.html", obats)
