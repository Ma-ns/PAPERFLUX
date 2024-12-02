from app.repositories.role_repository import RoleRepository
from app.models.role import Role
from app.models.user import User
from app import db

class RoleService:
    def __init__(self):
        self.role_repo = RoleRepository()

    def create_role(self, name, description=None):
        if self.role_repo.role_exists(name):
            raise ValueError("O nome do cargo já está em uso.")

        new_role = Role(name=name, description=description)
        self.role_repo.add(new_role)
        return new_role

    def get_role(self, role_id):
        return self.role_repo.get(role_id)

    def update_role(self, role_id, name=None, description=None):
        role = self.role_repo.get(role_id)

        if not role:
            return None

        if name:
            role.name = name
        if description:
            role.description = description

        self.role_repo.update(role)
        return role

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
