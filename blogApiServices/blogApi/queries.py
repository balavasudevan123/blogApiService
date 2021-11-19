import graphene
from .models import Blog, Comment
from .types import BlogFields, CommentFields

class Queries(graphene.ObjectType):
    allPosts = graphene.List(BlogFields)
    allComments = graphene.List(CommentFields)
    post = graphene.Field(BlogFields, postId=graphene.Int())

    def resolve_allPosts(self, info, **kwargs):
        return Blog.objects.all()

    def resolve_post(self, info, postId):
        return Blog.objects.get(id=postId)
    
    def resolve_allComments(self, info):
        return Comment.objects.all()