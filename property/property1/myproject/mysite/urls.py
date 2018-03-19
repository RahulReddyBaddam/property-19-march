from django.conf.urls import url,include
from mysite import views as view1
from accounts import views
from django.contrib.auth.views import login,logout


urlpatterns = [
    url(r'home/result$',view1.search,name='result'),
    url(r'home/$',view1.Home,name='home'),
    url(r'login/$',login,{'template_name': 'accounts/login.html'}),
    url(r'logout/$',logout, {'next_page': '/home/'}),
    url(r'register/$',views.register,name='register'),
    url(r'profile/$',views.view_profile,name='view_profile'),
    url(r'profile/(?P<pk>\d+)/$',views.view_profile,name='view_profile_pk'),
    url(r'profile/edit/$',views.update_profile, name ='update_profile'),
    url(r'addsite/$',views.addSite,name='addsite'),
    url(r'site/(?P<pk>\d+)/update/$',views.updateSite,name='update_site'),
    url(r'site/$',views.view_sites,name='view_sites'),
    url(r'site/(?P<pk>\d+)/delete/$',views.delete_site,name='delete_site'),
]
