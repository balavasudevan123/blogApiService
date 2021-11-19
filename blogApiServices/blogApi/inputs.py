import graphene

class PostInput(graphene.InputObjectType):
    id = graphene.ID()
    title = graphene.String()
    description = graphene.String()
    publish_date = graphene.String()
    author = graphene.String()

class CommentInput(graphene.InputObjectType):
    postIdMapping = graphene.Int(required=True)
    author = graphene.String()
    comment = graphene.String()