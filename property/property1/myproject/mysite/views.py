from django.shortcuts import render
from mysite.models import Site
from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.db.models import Q
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def Home(request):
    sites = Site.objects.all().order_by('-created_date')
    return render(request,'mysite/home.html',{'sites':sites})

@login_required
def search(request):
    query = request.GET.get("q")
    if query:
        items = Site.objects.filter(Q(title__icontains=query)|Q(category__icontains=query)|Q(descrip__icontains=query)).distinct().order_by('-created_date')


    return render(request,'mysite/home.html',{'items':items})
