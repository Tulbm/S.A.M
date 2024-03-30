from django.shortcuts import render
from django.http import JsonResponse
from oasis_app import backend

# Create your views here.

def index(request):
    return render(request, 'index.html')

# def prompt(request):
#     if request.method == 'POST':
#         prompt1 = request.POST.get('prompt1')
#         feeling = request.POST.get('feeling')
#         stress_level = request.POST.get('stress_level')

#         result = {
#             'prompt1': prompt1,
#             'feeling': feeling,
#             'stress_level': stress_level,
#             'dummy_response': f'{prompt1}, {feeling} and {stress_level}.'
#         }
#         return JsonResponse(result)
#     else:
#         return JsonResponse({'error': 'Invalid request method'})
    

def prompt(request):
    if request.method == 'POST':
        prompt1 = request.POST.get('prompt1')
        feeling = request.POST.get('feeling')
        stress_level = request.POST.get('stress_level')
        print('---------DEBUG------------')
        print(f'{prompt1}, {feeling}, {stress_level}')
        print('---------DEBUG------------')
        score = backend.predict(prompt1, feeling, stress_level)
        topics = backend.topics(prompt1)
        print('---------DEBUG------------')
        print(score)
        print(topics)
        print('---------DEBUG------------')

        if(score >= 0.6):
            response = backend.generate_bad(prompt1)
            print(response)
        else:
            response = "You are interested in: " + ", ".join(topics)
        result = {
            'prompt1': prompt1,
            'feeling': feeling,
            'stress_level': stress_level,
            'dummy_response': f'{response}'
        }
        return JsonResponse(result)
    else:
        return JsonResponse({'error': 'Invalid request method'})