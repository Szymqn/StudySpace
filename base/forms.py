from django import forms
from .models import Project, Topic


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'source_code']


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['name', 'content']

