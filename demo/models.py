from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=225, null=False, blank=False)
    author = models.CharField(max_length=225)
    price = models.FloatField()
    created_by = models.CharField(max_length=225)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Book"
