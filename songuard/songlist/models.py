from django.db import models

# Create your models here.
class Song(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    text = models.TextField()
    notes = models.TextField()
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.title
