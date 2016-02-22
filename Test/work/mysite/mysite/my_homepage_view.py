from django.http import HttpResponse

def my_homepage_view(request):
	return HttpResponse("My home page!")