import random
from app.db.database import Base, get_session
from typing import Type


def is_valid_instance_id(instance_id: int, class_model: Type[Base]):
    return get_session().query(class_model).filter(class_model.id == instance_id).one_or_none()


def last_data_in_the_table(class_model: Type[Base]):
    data = get_session().query(class_model).all()[-1]
    return data.id


def get_random_register_from_table(table: Type[Base]) -> Type[Base]:
    rand = random.randrange(0, get_session().query(table).count())
    if not(is_valid_instance_id(rand, table)):
        return get_random_register_from_table(table)
    return get_session().query(table)[rand]
