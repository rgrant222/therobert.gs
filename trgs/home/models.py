from django.db import models

# Create your models here.
class Hyperlink(models.Model):
  text = models.CharField(max_length=200)
  href = models.SlugField(max_length=200)

  def __unicode__(self):
    return u'%s' % self.text

