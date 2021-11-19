import graphene
from .inputs import PostInput, CommentInput
from .models import Blog, Comment
from .types import BlogFields, CommentFields

#CreatePost Class to create a new post
class CreatePost(graphene.Mutation):
    class Arguments:
        postData = PostInput(required=True)

    posts = graphene.Field(BlogFields)

    @staticmethod
    def mutate(root, info, postData=None):
        postInstance = Blog( 
            title=postData.title,
            description=postData.description,
            publish_date=postData.publish_date,
            author=postData.author
        )
        postInstance.save()
        return CreatePost(posts=postInstance)

#UpdatePost Class to update a particular existing post
class UpdatePost(graphene.Mutation):
    class Arguments:
        postData = PostInput(required=True)

    posts = graphene.Field(BlogFields)
    @staticmethod
    def mutate(root, info, postData=None):
        postInstance = Blog.objects.get(pk=postData.id)

        if postInstance:
            postInstance.title = postData.title
            postInstance.description = postData.description
            postInstance.publish_date = postData.publish_date
            postInstance.author = postData.author
            postInstance.save()

            return UpdatePost(posts=postInstance)
        return UpdatePost(posts=None)

#DeletePost Class to delete an existing post with the comments
class DeletePost(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
    
    posts = graphene.Field(BlogFields)

    @staticmethod
    def mutate(root, info, id):
        postInstance = Blog.objects.get(pk=id)
        postInstance.delete()

        return None

#CreateComment Class to write a new comment
class CreateComment(graphene.Mutation):
    class Arguments:
        postCommentData = CommentInput(required=True)

    postComments = graphene.Field(CommentFields)

    def mutate(root, info, postCommentData=None):
        postData = postCommentData.postIdMapping
        
        postIdMap_obj = Blog.objects.get(id=postData)
        commentInstance = Comment(
            postIdMap=postIdMap_obj,
            author=postCommentData.author,
            comment=postCommentData.comment
        )
        commentInstance.save()
        return CreateComment(postComments=commentInstance)

#DeleteComment Class to delete an existing comment by id
class DeleteComment(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
    
    comments = graphene.Field(CommentFields)

    @staticmethod
    def mutate(root, info, id):
        commentInstance = Comment.objects.get(pk=id)
        commentInstance.delete()
        
        return None

class Mutation(graphene.ObjectType):
    create_post = CreatePost.Field()
    update_post = UpdatePost.Field()
    delete_post = DeletePost.Field()
    add_comment = CreateComment.Field()
    delete_comment = DeleteComment.Field()