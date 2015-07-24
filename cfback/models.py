from django.db import models
from django.contrib.auth.models import User


class City(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name
    
class Sector(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name
    
class Company(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=75)
    city = models.ForeignKey(City)
    sector = models.ForeignKey(Sector)
    description = models.TextField()

    def __unicode__(self):
        return self.name

class Employee(models.Model):
    user = models.ForeignKey(
        User)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=75)
    company = models.ForeignKey(Company)
    department = models.CharField(max_length=100)

    class Meta:
        permissions = (
            ('can_delete_feedbacks', 'Can delete feedbacks'),
            ('can_view_feedbacks', 'Can view feedbacks'),
            )

    def __unicode__(self):
        return '%s  %s' % (
            self.user.username,
            self.user.get_full_name()
        )

class Customer(models.Model):
    user = models.ForeignKey(
        User)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=75)
    city = models.ForeignKey(City)

    class Meta:
        permissions = (
            ('can_add_feedbacks', 'Can add feedbacks'),
            )

    def __unicode__(self):
        return '%s %s' % (
            self.user.username,
            self.user.get_full_name()
        )

class FeedbackManager(models.Manager):
    def pending(self):
        qs = super(FeedbackManager, self).get_query_set()
        return qs.filter(models.Q(status=Property.PENDING) |
                         models.Q(status=Property.RESOLVED))
    

class Feedback(models.Model):
    PENDING,RESOLVED = range(2)
    FEEDBACK_STATUS = (
        (PENDING,'Pending'),
        (RESOLVED, 'Resolved'),
        )
    title = models.CharField(max_length=100)
    feed_back = models.TextField(verbose_name='feed back')
    date_posted = models.DateTimeField(verbose_name='date posted',auto_now_add=True)
    customer = models.ForeignKey(Customer)
    company = models.ForeignKey(Company)
##    status = models.PositiveSmallIntegerField(null = True ,choices=FEEDBACK_STATUS, blank = True)
    status = models.BooleanField(default=False)
    objects = FeedbackManager()

    def __unicode__(self):
        return self.title

class Faq(models.Model):
    question = models.CharField(max_length=500)
    answer = models.TextField()

    def __unicode__(self):
        return self.question

class Team(models.Model):
    name = models.CharField(max_length=100)
    pic = models.ImageField(upload_to='cfback/team')
    position = models.CharField(max_length=100)
    description = models.TextField()
    email = models.EmailField(max_length=75)
    twitter = models.URLField(max_length=100)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Team'
    
