from rest_framework import serializers
from .models import BlogModel


class BlogSerializers(serializers.ModelSerializer):
    class Meta:
        model = BlogModel
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogModel
        fields = ('__all__')
        extra_kwargs = {
            'security_question': {'write_only': True},
            'security_question_answer': {'write_only': True},
            'password': {'write_only': True}
        }
