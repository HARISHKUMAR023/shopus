from django.shortcuts import render
from  .models import porducts

# Create your views here.
def index(request):
    products_objects = porducts.objects.all()
    return render(request,'index.html',{'products_objects': products_objects})