from django.shortcuts import render

# Create your views here.
from cities.models import City

__all__= ('home')

def home(request, pk=None):
    if pk:
        city = City.objects.filter(id=pk).first()
        context = {'objects': city}
        return render(request, 'cities/home.html', context)
    qs = City.objects.all()
    context ={'objects_list':qs}
    return render(request, 'cities/home.html',context)

