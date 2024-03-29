from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    content = models.TextField()

    def __str__(self):
        return f'{self.title}'
    
    def contents(self):
        return self.content[:100]