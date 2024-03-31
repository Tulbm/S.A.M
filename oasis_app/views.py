from django.shortcuts import render, redirect
from django.http import JsonResponse
from oasis_app import backend
from django.views.decorators.csrf import csrf_exempt
from .models import Prompt
import asyncio
from oasis_app import backend
import test
from oasis_app import text_generation
import requests
import time

async def main(prompt1, feel):
    result = await text_generation.generate_bad(prompt1, feel)
    return result

def index(request):
    return render(request, 'index.html')

def prompt(request):
    if request.method == 'POST':
        prompt1 = request.POST.get('prompt1')
        feel = request.POST.get('feeling')
        stress = request.POST.get('stress_level')
        
        print('---------DEBUG------------')
        print(f'{prompt1}, {feel}, {stress}')
        stress = int(stress)  
        print('---------DEBUG------------')


        async def test_predict():
            text = prompt1
            feeling = feel
            stress_level = stress
            result = await test.predict(text, feeling, stress_level)
            print("Result:", result)
        asyncio.run(test_predict())

        result = asyncio.run(main(prompt1, feel))
        response_data = {
            'prompt1': prompt1,
            'feel': feel,
            'stress': stress,
            'result': result,
            'dummy_response': f'{prompt1}, {feel} and {stress}. | {result}'
        }
        print(response_data['result'])
        time.sleep(1)
        return JsonResponse(response_data)
    else:
        return render(request, 'index.html')
    
async def analyze_data(prompt1, feeling, stress_level):
    score = backend.predict(prompt1, feeling, stress_level)
    topics = backend.topics(prompt1)
    await score
    print(score)
    if score is not None and score >= 0.6:
        response = await backend.generate_bad(prompt1)
    else:
        response = "You are interested in: " + ", ".join(topics)
    
    result = {
        'prompt1': prompt1,
        'feeling': feeling,
        'stress_level': stress_level,
        'dummy_response': response
    }
    
    return await result

