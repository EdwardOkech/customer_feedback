from __future__ import absolute_import
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division

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
from django.contrib.auth.decorators import login_required, permission_required
import datetime
from django.core.mail import send_mail
from io import BytesIO
from reportlab.lib.colors import *
from reportlab.pdfgen import canvas
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.charts.piecharts import Pie
from reportlab.graphics import shapes, renderPDF
import csv
from django.utils.encoding import smart_str
from cfback.models import *
from django.core.context_processors import csrf
from django.utils.functional import wraps





##class IndexView(generic.ListView):
##    template_name = 'cfback/index.html'
##    context_object_name = 'id'
##
##    def get_queryset(self):
##        return Company.objects.order_by('sector')
##
##class DashboardView(generic.ListView):
##    template_name = 'cfback/dashboard.html'
##    context_object_name = 'id'
##
##    def get_queryset(self):
##        return Feedback.objects.all()
##
##class FeedbackView(generic.DetailView):
##    model = Feedback
##    template_name = 'cfback/feedback.html'


def _show_users(request):
    """Return show_users setting; if it does not exist, initialize it."""
    s = request.session
    if not "show_users" in s:
        s["show_users"] = True
    return s["show_users"]

@login_required
def settings(request):
    """Settings screen."""
    s = request.session
    _show_users(request)
    if request.method == "POST":
        s["show_users"] = (True if "show_users" in request.POST else False)
    return render_to_response("cfback/settings.html", RequestContext(request))


def reminders(request):
    """Return the list of reminders for pending feedbacks."""
    reminders = Feedback.objects.filter(title=title, customer=request.user, status=True)
    return list(reminders) + list(Feedback.objects.filter(title=title, customer=request.user, status=True))


def index(request):
    feedback = Feedback.objects.all()
    return render_to_response('cfback/index.html' ,RequestContext(request,{'feedback':feedback}))
    



def dashboard(request):
    feedbacks = Feedback.objects.all()
    if not _show_users(request):
        feedbacks = feedbacks.filter(customer=request.user)
    return render_to_response('cfback/dashboard.html', RequestContext(request,{'feedbacks':feedbacks}))


    
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
        
        
def feedback_detail(request, feedback_id):
    feedback = get_object_or_404(Feedback, pk=feedback_id)
    return render(request, 'cfback/feedback.html', {'feedback':feedback})

def company_detail(request,company_id):
    company=get_object_or_404(Company, pk=company_id)
    return render(request, 'cfback/company.html', {'company':company})

def employee_detail(request,employee_id):
    employee=get_object_or_404(Employee, pk=employee_id)
    return render(request, 'cfback/employee.html', {'employee':employee})

def customer_detail(request,customer_id):
    customer=get_object_or_404(Customer, pk=customer_id)
    return render(request, 'cfback/customer.html', {'customer':customer})

def user_reg(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
                email=form.cleaned_data['email'],
                )
            return HttpResponseRedirect('/cfback/')
    else:
        form = UserRegistrationForm()
    variables = RequestContext(request, { 'form': form})
    return render_to_response('registration/registration.html', variables)


def add_feedback(request):
    form = FeedbackForm()
    if request.POST:
        form = FeedbackForm(data = request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('.')
    return render_to_response('cfback/add_feedback.html', RequestContext(request,
                                                                     {'form': form,
                                                                      'feedbacks': Feedback.objects.all()
                                                                      }))

def add_faq(request):
    form = FaqForm()
    if request.POST:
        form = FaqForm(data = request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('.')
    return render_to_response('cfback/add_faq.html', RequestContext(request, {'form':form,
                                                                               'faqs': Faq.objects.all()
                                                                               }))

def faq(request):
    faqs = Faq.objects.all()
    return render_to_response('cfback/faq.html' ,RequestContext(request,{'faqs':faqs}))
    

def delete_feedback(request, feedback_pk, pk=None):
    '''Delete feedbacks with primary key 'pk' or with pks in post'''
    if request.user.has_perm('can_delete_feedbacks'):
        if not pk:
            pk_list = request.POST.getlist('delete')
        else:
            pk_list = [pk]
        for pk in pk_list:
            Feedback.objects.get(pk=pk).delete()
        return HttpResponseRedirect('.', args=[feedback_pk])
    
    

def report_pdf(request):
    feedbacks = Feedback.objects.all()
##    import pygraphviz as P
##    A=P.AGraph() # init empty graph
##    # set some default node attributes
##    A.node_attr['style']='filled'
##    A.node_attr['shape']='circle'
##    # Add edges (and nodes)
##    A.add_edge(1,2)
##    A.add_edge(2,3)
##    A.add_edge(1,3)
##    A.layout() # layout with default (neato)
##    png=A.draw(format='png') # draw png
##    return HttpResponse(png, mimetype='image/png')
    pdf_data = open('cfback/feed.pdf','rb').read()
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="feedback.pdf"'
    

    buffer = BytesIO()
   
    p = Drawing(400,200)
##    p.add(String(300,175, "Feedbacks", textAnchor="middle"))
    pc = Pie()
    pc.x = 150
    pc.y = 50
    pc.data = [enumerate([i.title[0]]) for i in feedbacks]
    pc.labels = [str(y.company) for y in feedbacks]
    p.add(pc)
##    p.showPage()
    p.save()

    pdf = buffer.getvalue()
    buffer.close
    response.write(pdf)
    return render_to_response('cfback/feed_report.html', response)

def export_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition']  = 'attachement; filename=feedback.csv'
    write = csv.write(response, csv.excel)

    response.write(u'\ufeff'.encode('utf8'))
    write.writerow([
        smart_str(u"ID"),
        smart_str(u"TITLE"),
        smart_str(u"DATE_POSTED"),
        smart_str(u"CUSTOMER"),
        smart_str(u"COMPANY"),
        smart_str(u"STATUS"),
        ])
    for obj in queryset:
      write.writerow([
           smart_str(obj.pk),
           smart_str(obj.title),
           smart_str(obj.date_posted),
           smart_str(obj.customer),
           smart_str(obj.company),
           smart_str(obj.status),
           ])
      write.save(response)
      return response
      export_csv.short_description = u"Export CSV"

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/cfback/')
