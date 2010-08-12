from django.conf.urls import patterns, include, url
from cfback import views

##from django.contrib import admin
##admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project_manager.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

##    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.IndexView.as_view(), name='index'),
    #url(r'^user/(\w+)/$', views.dev_page, name='dev_page'),
    url(r'^(?P<pk>\d+)/$', views.FeedbackView.as_view(), name='feedback'),
    url(r'^(?P<pk>\d+)/$', views.EmployeeView.as_view(), name='employee'),
    url(r'^(?P<pk>\d+)/$', views.CustomerView.as_view(), name='customer'),
    url(r'^(?P<pk>\d+)/$', views.CompanyView.as_view(), name='company'),                   
    url(r'^add_feedback/$', views.add_feedback, name='add_feedback'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    
##    url(r'^registration/$', views.user_reg, name='user_reg'),
    
    url(r'^logout/$', views.logout_page, name='logout'),
)
