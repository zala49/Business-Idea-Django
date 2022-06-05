from django.db import models
from django.contrib.auth.models import User
from innovator.models import Idea

class Contact(models.Model):
	name = models.CharField(max_length=30)
	email = models.EmailField()
	contact = models.CharField(max_length=15)
	subject = models.CharField(max_length=254)
	message = models.TextField()
	inq_date = models.DateField(auto_now_add=True)

	class Meta:
		db_table = 'inquiry'


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE, related_name='ideadetails')
    innovator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='innovator', null=True)
    title = models.CharField(max_length=100) 
    duration = models.CharField(max_length=150)
    price = models.CharField(max_length=20)
    date = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'order'


class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    rating = models.CharField(max_length=30)
    message = models.TextField()
    date = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'feedback'