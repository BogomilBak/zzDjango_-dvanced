from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=15,
    )

    def __str__(self):
        return self.name


class Todo(models.Model):
    title = models.CharField(
        max_length=24,
    )

    description = models.TextField()

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title
