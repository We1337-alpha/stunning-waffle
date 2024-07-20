from django.db import models

# Create your models here.
class Todo(models.Model):
    text = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('text',)
        verbose_name_plural = 'Todo list'

    def __str__(self):
        return self.text