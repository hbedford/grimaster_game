import graphene
from app.controllers.user.user_controllers import UserControllers
from app.graphql.types.type import UserType


class CreateUser(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)

    user = graphene.Field(UserType)

    @staticmethod
    def mutate(_, info, name):
        user = UserControllers().create_user(name=name)
        return CreateUser(user=user)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field(name='CreateUser')
