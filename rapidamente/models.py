from django.db import models
from django_extensions.db.models import TimeStampedModel
import shortuuid
from django.core.urlresolvers import reverse
# Create your models here.

class ShortUrl(TimeStampedModel):
    url = models.URLField(max_length=250, help_text="i.e. http://www.yahoo.com")
    nickname = models.CharField(max_length=12, blank=True, null=True, help_text="Give a nickname to this url")
    slug = models.CharField(max_length=10, unique=True, default=shortuuid.ShortUUID().random(length=3))
    got_nickname = models.BooleanField(default=False)

    def __str__(self):
        return self.shortened

    def get_absolute_url(self):
        return reverse('rapidamente:detail',
                       args=[str(self.shortened)]
                )
