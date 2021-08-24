from django import forms
from .models import Topic,GoodTopic,BadTopic


class TopicForm(forms.ModelForm):

    class Meta:
        model   = Topic
        fields  = [ "comment","user" ]


class GoodTopicForm(forms.ModelForm):
    class Meta:
        model   = GoodTopic
        fields  = [ "user","target" ]


class BadTopicForm(forms.ModelForm):
    class Meta:
        model   = BadTopic
        fields  = [ "user","target" ]

