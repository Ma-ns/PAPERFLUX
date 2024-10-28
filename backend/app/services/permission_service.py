from app.repositories.permission_repository import PermissionRepository
from app.models.permission import Permission
from app import db

class PermissionService:
    def __init__(self):
        self.permission_repo = PermissionRepository()

    def assign_permission(self, user_id, folder_id):
        new_permission = Permission(user_id = user_id, folder_id = folder_id)

        self.permission_repo.add(new_permission)

        return new_permission
    
    def undesignate_permission(self, user_id, folder_id):
        permission = self.permission_repo.get(user_id, folder_id)

        if permission:
            self.permission_repo.delete(permission)
            return True
        
        return False