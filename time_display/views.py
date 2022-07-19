from django.http import HttpResponse
from datetime import datetime


# Create your views here.
def display_curr_time(request):
    curr_time = datetime.now().strftime('%H:%M:%S')
    return HttpResponse(f"Current time: {curr_time}")