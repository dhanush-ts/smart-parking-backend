from rest_framework import serializers
from features.models import User, Category, CategoryData

class CategoryDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryData
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    category_data = CategoryDataSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
    