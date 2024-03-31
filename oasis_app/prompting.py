from django.shortcuts import render
from django.http import JsonResponse
from oasis_app import backend
from django.views.decorators.csrf import csrf_exempt
from .models import Prompt
import asyncio
from oasis_app import backend
import test
from oasis_app import text_generation
import json

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

        async def main():
            text = prompt1
            feeling = feel

            result = await text_generation.generate_bad(text, feeling)
            print(result)
                

        generated_text = asyncio.run(main())

        return generated_text