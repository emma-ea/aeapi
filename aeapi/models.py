from django.db import models
import uuid

# Create your models here.
class AgePrediction(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    request_time = models.DateTimeField()
    image_input = models.TextField()
    results_output = models.TextField()

    def __str__(self):
        return str(self.uid)

