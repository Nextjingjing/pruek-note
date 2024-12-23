from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=999)
    pub_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

