from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request,'index.html',{})
def aboutus(request):
	return render(request,'about_us.html',{})
def contactus(request):
	return render(request,'contact_us.html',{})
def privacy(request):
	return render(request,'privacy.html',{})
def services(request):
	return render(request,'services.html',{})
def support(request):
	return render(request,'support.html',{})
