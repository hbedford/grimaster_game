import graphene
from app.graphql.types.type import UserType
from app.controllers.user.user_controllers import UserControllers
from app.models.model import User


class UsersQuery(graphene.ObjectType):
    all = graphene.List(UserType)

    def resolve_all(self, info) -> list[User]:
        return UserControllers().get_users()


class Query(graphene.ObjectType):
    users = graphene.Field(UsersQuery, resolver=lambda _, __: UsersQuery)

    def resolve_hello(self, info, name):
        if name:
            return 'hello'

        return f"hello, {name}!!!"
