from django.shortcuts import render
from django.http import JsonResponse
from oasis_app import backend
from django.views.decorators.csrf import csrf_exempt
from .models import Prompt
import asyncio
from oasis_app.views import backend  # Import your backend module here



def index(request):
    return render(request, 'index.html')

def prompt(request):
    if request.method == 'POST':
        prompt1 = request.POST.get('prompt1')
        feeling = request.POST.get('feeling')
        stress_level = request.POST.get('stress_level')
        
        print('---------DEBUG------------')
        print(f'{prompt1}, {feeling}, {stress_level}')
        print('---------DEBUG------------')
        analyze_data(prompt1, feeling, stress_level)

        return JsonResponse({'success': 'ok'}, status=200)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
    
async def analyze_data(prompt1, feeling, stress_level):
    score = backend.predict(prompt1, feeling, stress_level)
    topics = backend.topics(prompt1)
    await score

    if score is not None and score >= 0.6:
        response = backend.generate_bad(prompt1)
    else:
        response = "You are interested in: " + ", ".join(topics)
    
    result = {
        'prompt1': prompt1,
        'feeling': feeling,
        'stress_level': stress_level,
        'dummy_response': response
    }
    
    return await result

