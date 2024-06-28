from rest_framework import serializers
from .models import Box

class BoxSerializer(serializers.ModelSerializer):
    area = serializers.ReadOnlyField()
    volume = serializers.ReadOnlyField()

    class Meta:
        model = Box
        fields = ['id', 'length', 'breadth', 'height', 'area', 'volume', 'created_by', 'created_at', 'updated_at']
        read_only_fields = ['created_by', 'created_at', 'updated_at']

class BoxListSerializer(BoxSerializer):
    created_by = serializers.StringRelatedField()

class MyBoxSerializer(BoxSerializer):
    pass
