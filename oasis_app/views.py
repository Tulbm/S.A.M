from django.shortcuts import render
from django.http import JsonResponse
from oasis_app import backend

# Create your views here.

def index(request):
    return render(request, 'index.html')

def prompt(request):
    if request.method == 'POST':
        prompt1 = request.POST.get('prompt1')
        feeling = request.POST.get('feeling')
        stress_level = request.POST.get('stress_level')
        score = backend.predict(prompt1, feeling, stress_level)
        topics = backend.topics(prompt1)
        if(score >= 0.6):
            response = generate_bad(prompt1)
        else:
            response = "You are interested in: " + ", ".join(topics)
        result = {
            'prompt1': prompt1,
            'feeling': feeling,
            'stress_level': stress_level,
            'dummy_response': f'{response}'
        }
        return JsonResponse(result)
