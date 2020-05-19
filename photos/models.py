from django.db import models

COPYRIGHT = "RIG"
COPYLEFT = "LEF"
CREATIVE_COMMONS = "CC"

LICENSES = (
    (COPYRIGHT, 'Copyright'),
    (COPYLEFT, 'Copyleft'),
    (CREATIVE_COMMONS, 'Creative Commons')
)

# Create your models here.


class Photo(models.Model):
    name = models.CharField(max_length=150)
    url = models.URLField()
    description = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    licenses = models.DateTimeField(auto_now=True, choices=LICENSES)
