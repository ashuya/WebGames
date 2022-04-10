from django.shortcuts import render

def index(request):
	context = {

			}
	return render(request, 'perudo/index.html', context)
