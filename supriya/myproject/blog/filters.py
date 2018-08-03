from django.contrib.auth.models import User
import django_filters
from django.db import models
from .models import Post

class PostFilter(django_filters.FilterSet):
	title = django_filters.CharFilter(lookup_expr='icontains')
	class Meta:
		model = Post
		fields = ['title',]

'''
class UserFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = ['username', ]
        '''

