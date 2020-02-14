from django.shortcuts import render
from .models import Instrument
# Create your views here.

def homepage(request):
    """
    A homepage for the website
    """
    ##If they have clicked learn more then redirect them to the instruments page
    if request.method == "POST":

        return instrument_page(request)
    instrument_list = get_instruments()
    instrument = Instrument.objects.get(name ="Guitar")
    print(instrument.instrument_image.path)


    context = {
        'instrument_list': instrument_list
    }
    return render(request, 'home.html', context)

def instrument_page(request):
    chosen_instrument = None
    request_post = request.POST
    #Choose the instrument that has been requested
    instrument_list = get_instruments()
    for instrument in instrument_list:
        if instrument["name"] in request_post:
            chosen_instrument = instrument
    context = {
        'instrument': chosen_instrument
    }

    return render(request, 'instrument_page.html',context)


def get_instruments():
    instrument_set = Instrument.objects.values()
    instrument_list = [instrument for instrument in instrument_set]
    return instrument_list
