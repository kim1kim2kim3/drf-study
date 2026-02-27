from django.http import JsonResponse
# Create your views here.

def api_home(request, *args, **kwargs):
    return JsonResponse({"message": "Hi there, This is your Django APi response"})