from django.forms import ModelForm, CharField, TextInput
from .models import Tag, Quote


class TagForm(ModelForm):

    name = CharField(min_length=3, max_length=25, required=True, widget=TextInput())
    
    class Meta:
        model = Tag
        fields = ['name']

class QuoteForm(ModelForm):

    author = CharField(min_length=5, max_length=50, required=True, widget=TextInput())
    text = CharField(min_length=10, max_length=280, required=True, widget=TextInput())

    class Meta:
        model = Quote
        fields = ['author', 'text']
        exclude = ['tags']
