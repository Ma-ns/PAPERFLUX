from werkzeug.security import generate_password_hash, check_password_hash
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

    def create_user(self, name, email, password, is_admin, file, role_id):
        path = self.file_service.upload_file(file, name,PROFILE_PICTURE_FOLDER)

        if self.user_repo.email_exists(email):
            raise ValueError("O e-mail já está em uso.")
        
        hashed_password = generate_password_hash(password)
        
        new_user = User(
            name = name, 
            email = email, 
            password_hash = hashed_password, 
            is_admin = is_admin, 
            profile_pic_path = path,
            role_id = role_id)

        self.user_repo.add(new_user) 

        return new_user
    
    def get_user(self, user_id):
        return self.user_repo.get(user_id)
    
    def get_all_users(self):
        return self.user_repo.get_all()
    
    def update_user(self, user_id, 
                    name = None, 
                    email = None, 
                    password = None, 
                    is_admin = None, 
                    profile_pic_path = None):
        
        user = self.user_repo.get(user_id)

        if not user:
            return None
        
        if name:
            user.name = name
        if email:
            user.email = email
        if password:
            hashed_password = generate_password_hash(password)
            user.password_hash = hashed_password
        if is_admin:
            user.is_admin = is_admin
        if profile_pic_path:
            user.profile_pic_path = profile_pic_path

        self.user_repo.update(user)

        return user
    
    def delete_user(self, user_id):
        user = self.user_repo.get(user_id)

        if user:
            self.user_repo.delete(user)
            return True
        
        return False

    def validate_login(self, email, password):
        user = self.user_repo.get_user_by_email(email)

        if check_password_hash(user.password_hash, password):
            return user
        
        return None