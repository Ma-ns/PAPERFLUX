from flask import jsonify, request
from app.services.user_service import UserService
from app.services.file_service import FileService

PROFILE_PICTURE_FOLDER = 'profile_pictures/'
ALLOWED_MIMES = {'image/png', 'image/gif', 'image/jpeg'}

class UserController:
    def __init__(self):
        self.user_service = UserService()
        self.file_service = FileService()

    def create_user(self):
        data = request.form

        file = request.files['file']

        name = data.get("name")
        email = data.get("email")
        password = data.get("password")
        is_admin = data.get("is_admin")

        if not name or not email or not password:
            return jsonify({"error": "Os Campos de nome, email e senha são obrigatórios"})

        try:
            new_user = self.user_service.create_user(name, email, password, is_admin, file)
            return jsonify({
            "message": "Usuário criado com sucesso!",
            "user": new_user.to_dict()
            }), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
    
    def get_user(self, user_id):
        user = self.user_service.get_user(user_id)

        if user:
            return jsonify(user.to_dict())
        
        return jsonify({"message": "Pasta não encontrada."}), 404
    
    def update_user(self, user_id):
        user = self.user_service.get_user(user_id)

        if not user:
            return jsonify({"message": "Usuário não encontrado"})

        data = request.get_json()

        name = data.get("name")
        email = data.get("email")
        password = data.get("password")
        is_admin = data.get("is_admin")

        updated_user = self.user_service.update_user(user_id, name, email, password, is_admin)
        
        if updated_user:
            return jsonify({
                "message": "Usuário atualizado com sucesso!",
                "user": updated_user.to_dict()
            })
        return jsonify({"message": "Não foi possível atualizar o usuário"})
    
    def update_profilePic(self, user_id):
        user = self.user_service.get_user(user_id)

        if not user:
            return jsonify({"message": "Usuário não encontrado"})
        
        file = request.files['file']

        path = self.file_service.update_file(file, user.name, user.profile_pic_path, PROFILE_PICTURE_FOLDER)
        updated_user = self.user_service.update_user(user_id, profile_pic_path=path)

        if path and updated_user:
            return jsonify({"message": "Foto de perfil atualizada com sucesso!"})
        return jsonify({"message": "Não foi possível atualizar a foto de perfil do usuário"})
        
    def delete_user(self, user_id):
        response = self.user_service.delete_user(user_id)

        if response:
            return jsonify({"message": "Usuário excluído com sucesso"}), 200
        return jsonify({"message": "Usuário não encontrado"}), 404
    
    def validate_login(self):
        data = request.get_json()

        email = data.get('email')
        password = data.get('password')
        
        user = self.user_service.validate_login(email, password)

        if user:
            return jsonify({
                "message": "Usuário logado com sucesso!",
                "user": user.to_dict()
            })
        return jsonify({"message": "Usuário inválido"})