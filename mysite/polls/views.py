from django.shortcuts import render
from django.http import HttpResponse
import sys
print(sys.path)

# Create your views here.
def index(request):
	return HttpResponse("Hey! Samar. Your are at the poll index.")