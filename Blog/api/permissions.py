from rest_framework import permissions
from django.contrib.auth.models import Group as Roles

class IsCreator(permissions.BasePermission):
	message = 'You are not the creator of this blog'

	def has_object_permission(self, request, view, obj):
		return obj.created_by==request.user