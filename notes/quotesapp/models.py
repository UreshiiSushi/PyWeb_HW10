from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=25, null=False, unique=True)

    def __str__(self):
        return f"{self.name}"


class Quote(models.Model):
    author = models.CharField(max_length=50, null=False)
    text = models.CharField(max_length=280, null=False)
    created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f"{self.text}"