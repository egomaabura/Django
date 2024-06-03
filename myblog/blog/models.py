from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self) -> str:
        return self.title