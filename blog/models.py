from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def summary(self):
        str = self.body[:100]
        if(str != self.body):
            str += '...'
        return str

    def pubDate(self):
        return self.pub_date.strftime('%b %e %Y')

    def __str__(self):
        return self.title


# Create your models here.
