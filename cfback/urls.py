from django.conf.urls import patterns, include, url
from cfback import views
##from rest_framework import routers
##from cfback.api import views

##from django.contrib import admin
##admin.autodiscover()


##router = routers.DefaultRouter()
##router.register(r'feedbacks', views.FeedbackViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project_manager.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

##    url(r'^admin/', include(admin.site.urls)),
##    url(r'^', include(router.urls)),
    url(r'^$', views.index, name='index'),
    #url(r'^user/(\w+)/$', views.dev_page, name='dev_page'),
    url(r'^(?P<feedback_id>\d+)/$', views.feedback_detail, name='feedback'),
    url(r'^(?P<employee_id>\d+)/$', views.employee_detail, name='employee'),
    url(r'^(?P<customer_id>\d+)/$', views.customer_detail, name='customer'),
    url(r'^(?P<company_id>\d+)/$', views.company_detail, name='company'),                   
    url(r'^add_feedback/$', views.add_feedback, name='add_feedback'),
    url(r'^delete_feedback/$', views.delete_feedback, name='delete_feedback'),
    url(r'^delete_feedback/(\d+)/(\d+)/$', views.delete_feedback, name='delete_feedback'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^feed_report/$', views.report_pdf, name='feed_report'),
    url(r'^exports/$', views.export_csv, name='exports'),
    url(r'^settings/$', views.settings, name='settings'),
    url(r'^faq/$', views.faq, name='faq'),
    url(r'^add_faq/$', views.add_faq, name='add_faq'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    
    url(r'^registration/$', views.user_reg, name='user_reg'),
    
    url(r'^logout/$', views.logout_page, name='logout'),
)
