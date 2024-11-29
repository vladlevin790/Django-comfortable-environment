from django import forms
from .models import Questions

class QuestionForm(forms.ModelForm):
    name = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'ваше имя', 'class' : 'inp-question'}))
    phone_number = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'номер телефона', 'class' : 'inp-question'}))
    question = forms.CharField(label="", widget=forms.Textarea(attrs={'placeholder': 'ваш вопрос', 'class' : 'textarea-question'}))

    class Meta:
        model = Questions
        fields = ['name', 'phone_number', 'question']