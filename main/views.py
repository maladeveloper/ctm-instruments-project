from django.shortcuts import render
from .models import Instrument
# Create your views here.

def homepage(request):
    """
    A homepage for the website
    """
    instrument_set= Instrument.objects.values()
    instrument_list = [instrument for instrument in instrument_set]

    context = {
        'instrument_list': instrument_list
    }
    print(instrument_list)




    return render(request, 'home.html',context)