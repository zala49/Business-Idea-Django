from django import forms
from myadmin.models import Category, Subcategory


class CategoryForm(forms.ModelForm):
	class Meta:
		model = Category
		fields = '__all__'


class SubcategoryForm(forms.ModelForm):
	class Meta:
		model = Subcategory
		fields = '__all__'
