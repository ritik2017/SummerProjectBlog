from rest_framework import serializers
from Blog.models import Blog

class BlogSerializer(serializers.ModelSerializer):
	created_by = serializers.ReadOnlyField(source='created_by.username')
	class Meta:
		model = Blog
		fields = [
			'pk',
			'title',
			'body',
			'created_at',
			'created_by',
		]