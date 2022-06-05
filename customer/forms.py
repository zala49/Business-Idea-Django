from django import forms
from customer.models import Contact, Feedback


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = "__all__"
        exclude = ('user',)