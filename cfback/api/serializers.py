from django.core import serializers
from rest_framework import serializers
from cfback.models import Feedback

##class QuerySetSerializer(serializers.get_serializer('json')):
##    pass

class FeedbackSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Feedback
        fields = (
            'id','title','customer','company',
            )
