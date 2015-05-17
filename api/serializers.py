from rest_framework import serializers

from task.models import Task
from result.models import Result


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('title', 'description', 'completed')

class ResultSerializer(serializers.ModelSerializer):

    class Meta:
        model = Result
        fields = ('pps', 'minor_code', 'award_code','class_code', 'award')
