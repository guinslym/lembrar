from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from .models import ShortUrl, get_uuid

def ensure_that_the_slug_is_unique(slug):
    slug_values = ShortUrl.objects.values('slug')
    urls = [list(i.values())[0] for i in slug_values]
    if slug in urls:
        slug_in_db = True
        while slug_in_db:
            new_slug = get_uuid()
            if new_slug in urls:
                continue
            else:
                #it's not in the db
                return new_slug
    else:
        return slug

@receiver(pre_save, sender=ShortUrl)
def pre_save_shortened_url(sender, instance, **kwargs):
    """
    Ensure that the given url is unique
    """
    slug_values = ShortUrl.objects.values('slug')
    urls = [list(i.values())[0] for i in slug_values]
    instance.slug = ensure_that_the_slug_is_unique(instance.slug)
    instance.save()
