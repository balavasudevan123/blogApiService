from graphene_django import DjangoObjectType
from .models import Blog, Comment


class BlogFields(DjangoObjectType):
    class Meta:
        model = Blog
        fields = "__all__"

class CommentFields(DjangoObjectType):
    class Meta:
        model = Comment