from django.db import models
from django.urls import reverse


class Event(models.Model):
    title = models.CharField(max_length=200,default='')
    description = models.TextField(default='')
    start_time = models.DateField(default='')
   

    @property
    def get_html_url(self):
        url = reverse('event_edit', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'


