from graphene_sqlalchemy import SQLAlchemyObjectType
from app.models.model import User

class UserType(SQLAlchemyObjectType):
    class Meta:
        model = User