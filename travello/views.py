from django.shortcuts import render,  redirect
from .models import Destination
# Create your views here.
def index(request):
    if request.user.is_authenticated:
        dests = Destination.objects.all()
        return render(request, 'index.html', {'dests': dests}) #json format
    else:
        # 用户未登录
        return redirect('login')
