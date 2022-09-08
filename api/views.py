from django.http import JsonResponse

def home(request):
    return JsonResponse({'title': 'Build rooms', 'purpose': 'build good rooms'})