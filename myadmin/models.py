from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    cat_name = models.CharField(max_length=30)

    class Meta:
        db_table = 'category'

    def __str__(self):
        return self.cat_name


class Subcategory(models.Model):
    subcat_name = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        db_table = 'subcategory'

    def __str__(self):
        return self.subcat_name


class State(models.Model):
    state_name = models.CharField(max_length=100, null=False, blank=False)

    class Meta:
        db_table = 'state'

    def __str__(self):
        return self.state_name


class City(models.Model):
    city_name = models.CharField(max_length=100, null=False, blank=False)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    class Meta:
        db_table = 'city'

    def __str__(self):
        return self.city_name


class Role(models.Model):
    role = models.CharField(max_length=50)

    class Meta:
        db_table = 'role'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='innovatorprofile')
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    designation = models.CharField(max_length=100,  null=True)
    experience = models.CharField(max_length=10,  null=True)
    about = models.TextField(null=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True)
    address = models.TextField(null=True)
    contact = models.CharField(max_length=15, null=True)
    profile_photo = models.ImageField(upload_to='profiles', null=True)

    class Meta:
        db_table = 'profile'

    def __str__(self):
        return self.user

    def state_name(self):
        return self.state.state_name
