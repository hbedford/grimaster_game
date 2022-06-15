from app.controllers import Controller
from app.models.model import User


class UserControllers(Controller):
    def create_user(self, name: str) -> User:
        if not self.check_name_enable(name):
            raise Exception('Informe um nome com no minimo 3 caracteres')

        user = User(name=name)

        self.session.add(user)
        self.session.commit()
        return user

    def update_user_name(self, name: str, user_id: int) -> User:

        if self.get_user_id(user_id) is None:
            raise Exception('Não existe usuário com esse id')
        if not self.check_name_enable(name):
            raise Exception('Informe um nome com no minimo 3 caracteres')

        self.session.query(User, )

    @staticmethod
    def check_name_enable(self, name: str) -> bool:
        return name and len(name) > 3

    def get_user_id(self, user_id: int) -> User | None:
        return self.session.query(User).filter(User.id == user_id)
