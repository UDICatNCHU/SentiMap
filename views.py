from django.http import HttpResponse
from django.shortcuts import render_to_response, render

def map(request, MapName):
	MapName += '.js'
	return render_to_response('SentiMap/taiwan.html',locals())

def relation(request, MapName):
	MapName += '.js'
	return render_to_response('SentiMap/relation.html',locals())