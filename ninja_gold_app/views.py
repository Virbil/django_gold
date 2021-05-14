from django.shortcuts import redirect, render
import random as rand
import datetime
from django.forms import HiddenInput

from datetime import datetime

today = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

def index(request):
    if 'rupees' not in request.session:
        request.session['rupees'] = 0
    if 'activity_log' not in request.session:
        request.session['activity_log'] = ''
    
    return render(request,'index.html')

def farm(request):
    request.session['rupees'] += rand.randrange(10, 20)
    request.session['activity_log'] += 'Earned ' + str(request.session['rupees']) + ' rupees from the farm! ' + str(today)
    request.session['activity_log'] += '\n'

    return render(request, 'index.html')

def cave(request):
    request.session['rupees'] += rand.randrange(5, 10)
    request.session['activity_log'] += 'Earned ' + str(request.session['rupees']) + ' rupees from the cave! ' + str(today)
    return render(request, 'index.html')

def house(request):
    request.session['rupees'] += rand.randrange(2, 5)
    request.session['activity_log'] += 'Earned ' + str(request.session['rupees']) + ' rupees from the house! ' + str(today)
    return render(request, 'index.html')

def casino(request):
    request.session['rupees'] += rand.randrange(-50, 50)
    if request.session['rupees'] < 0:
        request.session['activity_log'] += 'Entered a casino and lost ' + str(request.session['rupees']) + '. Ouch! That might teach you to gamble.' + str(today)
    else:
        request.session['activity_log'] += 'It is your lucky day. You entered a casino and won ' + str(request.session['rupees']) + ' rupees!' + str(today)
    return render(request, 'index.html')

def process_rupees(request):
    request.session.flush()
    return render(request,'index.html')