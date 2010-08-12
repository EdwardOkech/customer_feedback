from django.shortcuts import get_object_or_404, render_to_response,render, Http404
from django.http import HttpResponse
from cfback.forms import *
from django.template import RequestContext, loader
from django.template.loader import get_template
##from django.template import Context
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import datetime
from django.core.mail import send_mail
from django.views import generic

from cfback.models import *



class IndexView(generic.ListView):
    template_name = 'cfback/index.html'
    context_object_name = ['id','name','email','city','sector']

    def get_queryset(self):
        return Company.objects.order_by('sector')

class FeedbackView(generic.DetailView):
    model = Feedback
    template_name = 'cfback/feedback.html'


class CustomerView(generic.DetailView):
    model = Customer
    template_name = 'cfback/customer.html'


class CompanyView(generic.DetailView):
    model = Company
    template_name = 'cfback/company.html'

class EmployeeView(generic.DetaiView):
    model = Employee
    template_name = 'cfback/employee.html'

    
##def index(request): 
##    customer_name = request.user.first_name
##    customer_feedback = Feedback.feed_back
##    customer_city = Customer.city
##    feed_posted = Feedback.date_posted
##    return render_to_response('cfback/index.html', RequestContext(request,
##                                                                  {'customer_name':customer_name,
##                                                                   'customer_feedback': customer_feedback,
##                                                                   'customer_city': customer_city,
##                                                                   'feed_posted': feed_posted
##                                                                   }
##                                                                  ))
        
        

####def company_detail(request,company_id):
####    company=get_object_or_404(Company, pk=company_id)
####    return render(request, 'cfback/company.html', {'company':company})
####
####def employee_detail(request,employee_id):
####    employee=get_object_or_404(Employee, pk=employee_id)
####    return render(request, 'cfback/employee.html', {'employee':employee})
####
####def customer_detail(request,customer_id):
####    customer=get_object_or_404(Customer, pk=customer_id)
####    return render(request, 'cfback/customer.html', {'customer':customer})

##def user_reg(request):
##    if request.method == 'POST':
##        form = UserRegistrationForm(request.POST)
##        if form.is_valid():
##            user = User.objects.create_user(
##                username=form.cleaned_data['username'],
##                password=form.cleaned_data['password1'],
##                email=form.cleaned_data['email'],
##                )
##            return HttpResponseRedirect('/cfback/')
##    else:
##        form = UserRegistrationForm()
##    variables = RequestContext(request, { 'form': form})
##    return render_to_response('cfback/registration.html', variables)

def add_feedback(request):
    form = FeedbackForm()
    if request.POST:
        form = FeedbackForm(data = request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('.')
    return render_to_response('cfback/feedback.html', RequestContext(request,
                                                                     {'form': form,
                                                                      'feedbacks': Feedback.objects.all()
                                                                      }))
    
    

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/cfback/')
