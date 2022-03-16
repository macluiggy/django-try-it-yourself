from django.db import models

# Create your models here.

class BlogPost(models.Model):
    """A single blog post."""
    title = models.CharField(max_length=100)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        """Return a string representation of the model."""
        return f"{self.title}"