from app.models.permission import Permission
from app import db

class PermissionRepository:
    def add(self, permission):
        db.session.add(permission)
        db.session.commit()

    def delete_user_permission(self, user_id):
        Permission.query.filter_by(user_id = user_id).delete()
        db.session.commit()

    def delete_folder_permission(self, folder_id):
        Permission.query.filter_by(folder_id = folder_id).delete()

    def get_user_permission(self, user_id):
        return Permission.query.filter_by(user_id = user_id).all()

    def get_folder_permission(self, folder_id):
        return Permission.query.filter_by(folder_id = folder_id).all()
