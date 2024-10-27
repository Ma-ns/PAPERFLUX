from app.repositories.user_repository import UserRepository
from .file_service import FileService
from app.models.user import User
from app import db

PROFILE_PICTURE_FOLDER = 'profile_pictures/'
ALLOWED_MIMES = {'image/png', 'image/gif', 'image/jpeg'}

class UserService:
    def __init__(self):
        self.user_repo = UserRepository()
        self.file_service = FileService()

    def create_user(self, name, email, password, is_admin, file):
        path = self.file_service.upload_file(file, name,PROFILE_PICTURE_FOLDER)

        new_user = User(name = name, email = email, password_hash = password, is_admin = is_admin, profile_pic_path = path)

        self.user_repo.add(new_user) 

        # validar se email já existe

        return new_user