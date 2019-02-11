from django import forms
from .models import Topic

class NewTopicForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(
            attrs = { 'rows':4 , 'placeholder':'This is where you type summary text'}
            ),
         help_text='This Input should not be greater than 4000 charecters',
         max_length=4000)
    class Meta:
        model = Topic
        fields =['subject', 'message']

