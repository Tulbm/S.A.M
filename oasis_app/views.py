from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def prompt(request):
    if request.method == 'POST':
        prompt1 = request.POST.get('prompt1')
        feeling = request.POST.get('feeling')
        stress_level = request.POST.get('stress_level')
        
        result = {
            'prompt1': prompt1,
            'feeling': feeling,
            'stress_level': stress_level,
            'dummy_response': f'{prompt1}, {feeling} and {stress_level}.'
        }
        return JsonResponse(result)
