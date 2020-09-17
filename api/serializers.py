from rest_framework import serializers
from .models import Content


class ContentSerializer(serializers.ModelSerializer):
    categories = serializers.StringRelatedField(many=True, read_only=True)
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Content
        fields = ("id", "title", "body", "summary",
                  "categories", "document", "owner")
        read_only_fields = ('owner',)
