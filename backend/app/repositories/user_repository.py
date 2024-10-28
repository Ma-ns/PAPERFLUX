from app.models.user import User
from .base_repository import BaseRepository
from app import db

class UserRepository(BaseRepository):
    def __init__(self):
        super().__init__(User)

    def email_exists(self, email):
        return db.session.query(User).filter_by(email=email).first()