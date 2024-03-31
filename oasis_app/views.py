from django.shortcuts import render
from django.http import JsonResponse
from oasis_app import backend
from django.views.decorators.csrf import csrf_exempt
from .models import Prompt
import asyncio
from oasis_app import backend
import test
from oasis_app import text_generation
import requests

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
            'result': result
        }
        print(response_data['result'])
        return render(request, 'index.html', response_data)
    else:
        # Handle GET requests here
        return render(request, 'index.html')
    
async def analyze_data(prompt1, feeling, stress_level):
    score = backend.predict(prompt1, feeling, stress_level)
    topics = backend.topics(prompt1)
    await score
    print(score)
    if score is not None and score >= 0.6:
        response = await backend.generate_response(text=prompt1, postive=False)
    else:
        prompt1 = "You are interested in: " + ", ".join(topics) + ". " + prompt1
        response = await backend.generate_response(text=prompt1, postive=True)
    
    result = {
        'prompt1': prompt1,
        'feeling': feeling,
        'stress_level': stress_level,
        'dummy_response': response
    }
    
    return await result

