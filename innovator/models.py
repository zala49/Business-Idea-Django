from django.db import models
from myadmin.models import Category, Subcategory
from innovator.validators import validate_file_extension
from django.conf import settings
from django.contrib.auth.models import User

class Idea(models.Model):
    STATUS = (
        ('active', 'Active'),
        ('inactive', 'In Active'),
    )
    title = models.CharField(max_length=254)
    small_description = models.TextField()
    large_description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    setup_price = models.CharField(max_length=20)
    setup_duration = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='uploads/', validators=[validate_file_extension])
    status = models.CharField(max_length=30, choices=STATUS, default='active')

    class Meta:
        db_table = 'idea'

    def __str__(self):
        return self.title
