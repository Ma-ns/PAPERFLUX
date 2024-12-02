from app.models.role import Role
from app.models.user import User
from app import db

class RoleRepository:
    def add(self, role):
        db.session.add(role)
        db.session.commit()

    def get(self, role_id):
        return Role.query.filter_by(id=role_id).first()

    def delete(self, role):
        db.session.delete(role)
        db.session.commit()

    def get_all(self):
        return Role.query.all()

    def get_users_by_role(self, role_id):
        return User.query.filter_by(role_id=role_id).all()
