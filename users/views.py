# users/views.py

from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from .utils.jwt_utils import generate_jwt

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            token = generate_jwt(user.id)
            return JsonResponse({'token': token})
        else:
            return JsonResponse({'error': 'Invalid credentials'}, status=401)

def logout_view(request):
    logout(request)
    return JsonResponse({'message': 'Logged out successfully'})

