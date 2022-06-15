import graphene
from starlette_graphene3 import GraphQLApp
from app.graphql.mutations.mutation import Mutation
from app.graphql.queries.query import Query

graphql_schema = graphene.Schema(query=Query, mutation=Mutation)

graphql_app = GraphQLApp(schema=graphql_schema,)
