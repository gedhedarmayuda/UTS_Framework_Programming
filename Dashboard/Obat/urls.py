from django.urls import path
from . import views

urlpatterns = [
    path('obat/list/', views.drug_list),
    path('obat/form/', views.drug_form),
]