from app.db.database import Base, engine


def create_data():
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    create_data()
