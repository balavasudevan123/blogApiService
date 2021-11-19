import graphene

from blogApi.mutations import Mutation as CoreMutations
from blogApi.queries import Queries as CoreQueries

class Query(
    CoreQueries,
):
    pass

class Mutation(
    CoreMutations,
):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)