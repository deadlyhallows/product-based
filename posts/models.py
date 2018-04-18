from  __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.



class Post(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(
        null=True,blank=True,
        height_field="height_field",
        width_field="width_field")
    height_field=models.IntegerField(default=0)
    width_field=models.IntegerField(default=0)
    content = models.TextField()
    timestamp = models.DateField(auto_now=False,auto_now_add=True)
    updated = models.DateField(auto_now=True,auto_now_add=False)

    def __unicode__(self):
        return self.title


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('posts:detail',kwargs={"id":self.id})

    class Meta:
        ordering = ['-timestamp','-updated']#important

