from django import forms
from .models import Topic

class NewTopicForm(forms.ModelForm):
    message = forms.name = models.CharField(widget=forms.Textarea, max_length=4000)
    class Meta:
        model = Topic
        fields =['subject', 'message']

