from django.shortcuts import render
from .models import CustomUser

# Example view: List all users
def user_list(request):
    users = CustomUser.objects.all()
    return render(request, 'accounts/user_list.html', {'users': users})
