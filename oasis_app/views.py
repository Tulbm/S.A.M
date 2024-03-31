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

        return JsonResponse({'success': 'ok'}, status=200)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

