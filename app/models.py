from django.db import models

# Create your models here.
class Topic(models.Model):
    topic_name=models.CharField(max_length=100)

    def __str__(self):
        return self.topic_name

class WebPages(models.Model):
    topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    url=models.URLField()

    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name=models.ForeignKey(WebPages,on_delete=models.CASCADE)
    date=models.DateField()
    author=models.CharField(max_length=100)

    def __str__(self):
        return self.author