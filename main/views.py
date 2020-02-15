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

    context = {
        'instrument_list': instrument_list
    }
    return render(request, 'home.html', context)

def instrument_page(request):
    chosen_instrument = None
    request_post = request.POST
    #Choose the instrument that has been requested

    #Get all instrument objects
    all_instruments = Instrument.objects.all()
    for instrument in all_instruments:
        if instrument.name in request_post:
            chosen_instrument = instrument
    print(chosen_instrument)
    print(chosen_instrument.youtube_code)

    context = {
        'instrument': chosen_instrument,
        'src': "https://www.youtube.com/embed/"+ chosen_instrument.youtube_code
    }

    return render(request, 'instrument_page.html',context)


def get_instruments():
    instrument_set = Instrument.objects.values()
    instrument_list = [instrument for instrument in instrument_set]
    return instrument_list
