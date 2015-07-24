from django.core import serializers
from rest_framework import viewsets
from cfback.api.serializers import FeedbackSerializer
from cfback.models import Feedback

##class QuerySetSerializer(serializers.get_serializer('json')):
##    pass

class FeedbackViewSet(viewsets.ModelViewSet):
    '''api endpoint that allows feedbacks to be viewed or edited'''
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
