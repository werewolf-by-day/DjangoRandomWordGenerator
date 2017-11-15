from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
  	return render(request, "rando/index.html")

def generate(request, method=["POST"]):
	request.session['word'] = get_random_string(length=14)
	if 'number' in request.session:
		request.session['number'] += 1
	else:
		request.session['number'] = 1
	return redirect ('/')

