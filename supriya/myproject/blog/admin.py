from django.contrib import admin
from .models import Post, Comment, Addlikes

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Addlikes)