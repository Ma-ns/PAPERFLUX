from app.repositories.role_repository import RoleRepository
from app.models.role import Role
from app.models.user import User
from app import db

class RoleService:
    def __init__(self):
        self.role_repo = RoleRepository()

    def create_role(self, name):
        new_role = Role(name=name)
        self.role_repo.add(new_role)
        return new_role

    def get_role(self, role_id):
        return self.role_repo.get(role_id)

    def delete_role(self, role_id):
        role = self.role_repo.get(role_id)

        if role:
            self.role_repo.delete(role)
            return True

        return False

    def get_users_by_role(self, role_id):
        role = self.role_repo.get(role_id)

        if not role:
            return []

        return self.role_repo.get_users_by_role(role_id)
