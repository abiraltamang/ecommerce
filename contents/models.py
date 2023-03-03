from django.db import models

class Section(models.Model):
    title = models.CharField(max_length=255)
    caption = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Content(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    title   = models.CharField(max_length=255)
    details = models.TextField()
    image = models.ImageField(upload_to='contents', null=True, blank=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title
