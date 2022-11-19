from django.shortcuts import render
from Karyawan.models import *

# Create your views here.
def employee_list(request):
    karyawans = Karyawan.objects.all()
    
    konteks = {
        "karyawans":karyawans,
    }
    return render(request, "karyawan/list_karyawan.html", konteks)

