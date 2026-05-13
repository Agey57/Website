from django.db import models
from django.utils.timezone import now


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=256)
    text = models.TextField()
    published_at = models.DateTimeField(default=now)
    image = models.ImageField(upload_to='articles/', null=True, blank=True)

    tags = models.ManyToManyField(
        Tag,
        through='Scope',
        related_name='articles',
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-published_at']


class Scope(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.article} - {self.tag}"

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['article', 'tag'], name='unique_scope'),
        ]