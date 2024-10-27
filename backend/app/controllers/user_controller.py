from flask import jsonify, request
from app.services.user_service import UserService

class UserController:
    def __init__(self):
        self.user_service = UserService()

    def create_user(self):
        data = request.form

        file = request.files['file']

        name = data.get("name")
        email = data.get("email")
        password = data.get("password")
        is_admin = data.get("is_admin")

        if not name or not email or not password:
            return jsonify({"error": "Os Campos de nome, email e senha são obrigatórios"})
        
        new_user = self.user_service.create_user(name, email, password, is_admin, file)

        return jsonify({
            "message": "Usuário criado com sucesso!",
            "user": new_user.to_dict()
            }), 200
    
    def get_user(self):
        user = self.user_service.get_user()
    

