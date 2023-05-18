from django.shortcuts import render

# Create your views here.
def built_in_filters(request):
    d={'data':'kRiSHna wAs a SpirITUAL GoD '}
    return render(request,'built_in_filters.html',d)