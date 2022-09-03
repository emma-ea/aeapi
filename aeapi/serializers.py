from rest_framework import serializers
from . import models

class APSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.AgePrediction
        fields = ("uid", "request_time", "image_input", "results_output")

