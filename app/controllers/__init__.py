from sqlalchemy.orm import Session
from app.db.database import get_session


class Controller:
    def __init__(self, session: Session = get_session()):
        self.session = session
