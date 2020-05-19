from django.db import models

class Blog(models.Model):
    Title=models.CharField(max_length=100)
    image=models.ImageField(upload_to='images/')
    publishdate=models.DateTimeField()
    Body=models.TextField(default='Enter Text')
