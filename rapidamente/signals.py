from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import ShortUrl, get_uuid

def get_uuid():
    import shortuuid
    return shortuuid.ShortUUID().random(6)

def ensure_that_the_slug_is_unique(slug):
    slug_values = ShortUrl.objects.values('slug')
    urls = [list(i.values())[0] for i in slug_values]
    if slug in urls:
        #The slug is not unique
        slug_in_db = True
        while slug_in_db:
            #create a new slug (uuid)
            new_slug = get_uuid()
            if new_slug in urls:
                continue
            else:
                slug_in_db = False
                #it's not in the db
                return new_slug
    else:
        return slug

@receiver(pre_save, sender=ShortUrl)
def pre_save_shortened_url(sender, instance, **kwargs):
    """
    Ensure that the given url is unique
    """

    #import ipdb; ipdb.set_trace()
    response = instance.slug
    if ShortUrl.objects.filter(slug=response):
        response = get_uuid()
    instance.slug = response
    instance.save()
