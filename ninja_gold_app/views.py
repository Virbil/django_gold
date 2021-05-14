from django.shortcuts import redirect, render
import random as rand
import datetime
from django.forms import HiddenInput

from datetime import datetime

today = datetime.now().strftime("%m/%d/%Y %I:%M%p")

def index(request):
    if 'rupees' not in request.session or 'activity_log' not in request.session:
        request.session['rupees'] = 0
        request.session['activity_log'] = []
    
    return render(request,'index.html')

def farm(request):
    farm_add = rand.randrange(10, 20)
    farm_message = f"Earned {str(farm_add)} rupees from the farm! - {str(today)}"
    request.session['rupees'] += farm_add
    request.session['activity_log'].append({'message': farm_message})
    # <p>Earned {str(request.session['rupees'])} rupees from the farm! - {str(today)}</p>"
    return redirect('/')

def cave(request):
    cave_add = rand.randrange(5, 10)
    cave_message = f"Earned {str(cave_add)} rupees from the cave! - {str(today)}"
    request.session['rupees'] += cave_add
    request.session['activity_log'].append({'message': cave_message})
    return redirect('/')

def house(request):
    house_add = rand.randrange(2, 5)
    house_message = f"Earned {str(house_add)} rupees from the house! - {str(today)}"
    request.session['rupees'] += house_add
    request.session['activity_log'].append({'message': house_message})
    print(request.session['activity_log'])
    return redirect('/')

def casino(request):
    casino_change = rand.randrange(-50, 50)
    request.session['rupees'] += casino_change
    if casino_change < 0:
        casino_message = f"Entered a casino and lost {str(casino_change)} rupees. Ouch! That might teach you to gamble. - {str(today)}"
        request.session['activity_log'].append({'message': casino_message})
    else:
        casino_message = f"It is your lucky day. You entered a casino and won {str(casino_change)} rupees! - {str(today)}"
        request.session['activity_log'].append({'message': casino_message})
    return redirect('/')

def process_rupees(request):
    request.session.flush()
    return redirect('/')