from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from accounts.forms import RegistrationForm,EditProfileForm,ProfileForm,SiteForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from accounts.models import UserProfile
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from mysite.models import Site
from django.utils import timezone
from django.shortcuts import get_object_or_404
# Create your views here.

def view_sites(request):
    sites = Site.objects.filter(user=request.user).order_by('-created_date')
    return render(request,'accounts/site.html',{'sites':sites})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
    else:
        form = RegistrationForm()


    return render(request,'accounts/reg_form.html',{'form':form})


@login_required
def view_profile(request,pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user=request.user

    args = {'user':user}
    return render(request,'accounts/profile.html',args)

@login_required
def update_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.userprofile)
        if form.is_valid() and profile_form.is_valid():
            form.save()
            profile_form.save()
            return redirect('/profile')
    else:
        form = EditProfileForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.userprofile)
    return render(request, 'accounts/edit_profile.html', {
        'form': form,
        'profile_form': profile_form
    })

@login_required
def addSite(request):
    if request.method == 'POST':
        form1  = SiteForm(request.POST)
        if form1.is_valid():
            u1 = form1.save(commit=False)
            u1.user=request.user
            u1.created_date = timezone.now()
            u1.save()
            return redirect('/profile')
    else:
        form1  = SiteForm()
    return render(request,'accounts/addsite.html',{
        'form1':form1,
    })


@login_required
def updateSite(request,pk=None):
    site = get_object_or_404(Site,pk=pk)
    Site.objects.get(pk=pk).delete()
    if request.method == 'POST':
        form1  = SiteForm(request.POST,instance=site)
        if form1.is_valid():
            st = form1.save(commit=False)
            st.user = request.user
            st.created_date = timezone.now()
            st.save()
            return redirect('/site')
    else:
        form1  = SiteForm(instance=site)

    return render(request,'accounts/update_site.html',{'form1':form1,})

def delete_site(request,pk=None):
    if pk:
        Site.objects.get(pk=pk).delete()
    else:
        pass
    return redirect('/site')
