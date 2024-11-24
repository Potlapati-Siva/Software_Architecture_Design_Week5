from django.shortcuts import render
from django.http import JsonResponse
def index(request):
    #The Model Objects should be accessed and use templates to prepare responses.
    return JsonResponse({"Message":"Hello World!"})
# Create your views here.




























