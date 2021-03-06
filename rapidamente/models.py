from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.core.urlresolvers import reverse
import datetime
from django.utils import timezone
# Create your models here.


def get_uuid():
    import shortuuid
    import random
    return shortuuid.ShortUUID().random(random.randint(3,6))

class ShortUrl(TimeStampedModel):
    url = models.URLField(max_length=250, help_text="i.e. http://www.yahoo.com")
    nickname = models.CharField(max_length=12, blank=True, unique=True, null=True, help_text="Give a nickname to this url")
    slug = models.CharField(max_length=10, unique=True, default=get_uuid)
    got_nickname = models.BooleanField(default=False)
    expiring_date = models.DateField(
                        default=(timezone.now() + datetime.timedelta(days=30)),
                        blank=True, null=True,
                        help_text="Select a date of Expiration." \
                        " By default it is set two 1 months")
    #expiring_date = 90 jours

    def __str__(self):
        return self.slug

    def get_absolute_url(self):
        return reverse('rapidamente:detail',
                       args=[str(self.slug)]
                )
