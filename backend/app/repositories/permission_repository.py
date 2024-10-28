from app.models.permission import Permission
from app.models.user import User
from app.models.folder import Folder
from app import db

class PermissionRepository:
    def add(self, permission):
        db.session.add(permission)
        db.session.commit()

    def get(self, user_id, folder_id):
        return Permission.query.filter(
        Permission.user_id == user_id,
        Permission.folder_id == folder_id
    ).first()

    def delete(self, permission):
        db.session.delete(permission)
        db.session.commit()

    def delete_all_user_permission(self, user_id):
        Permission.query.filter_by(user_id = user_id).delete()
        Permission.session.commit()

    def delete_all_folder_permission(self, folder_id):
        Permission.query.filter_by(folder_id = folder_id).delete()

    def get_all_user_permission(self, user_id):
        return Permission.query.filter_by(user_id = user_id).all()

    def get_all_folder_permission(self, folder_id):
        return Permission.query.filter_by(folder_id = folder_id).all()
