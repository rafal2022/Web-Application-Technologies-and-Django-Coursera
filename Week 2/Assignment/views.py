#add this file in the same directory where urls.py is located
from django.http import HttpResponse

def home(request):
	# add your individual unique string into the response
    return HttpResponse("Hello, world. 7da66e82 is the polls index.") 
