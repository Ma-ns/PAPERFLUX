from flask import jsonify, request
from app.services.role_service import RoleService

class RoleController:
    def __init__(self):
        self.role_service = RoleService()

    def create_role(self):
        data = request.get_json()

        name = data.get("name")

        if not name:
            return jsonify({"error": "O campo 'name' é obrigatório"})

        try:
            new_role = self.role_service.create_role(name)
            return jsonify({
                "message": "Cargo criado com sucesso!",
                "role": new_role.to_dict()
            }), 201
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
    
    def get_role(self, role_id):
        role = self.role_service.get_role(role_id)

        if role:
            return jsonify(role.to_dict())
        
        return jsonify({"message": "Cargo não encontrado."}), 404

    def update_role(self, role_id):
        role = self.role_service.get_role(role_id)

        if not role:
            return jsonify({"message": "Cargo não encontrado"})

        data = request.get_json()

        name = data.get("name")

        updated_role = self.role_service.update_role(role_id, name)
        
        if updated_role:
            return jsonify({
                "message": "Cargo atualizado com sucesso!",
                "role": updated_role.to_dict()
            })
        return jsonify({"message": "Não foi possível atualizar o cargo"}), 400

    def delete_role(self, role_id):
        response = self.role_service.delete_role(role_id)

        if response:
            return jsonify({"message": "Cargo excluído com sucesso"}), 200
        return jsonify({"message": "Cargo não encontrado"}), 404

    def get_users_by_role(self, role_id):
        users = self.role_service.get_users_by_role(role_id)

        if users:
            return jsonify([user.to_dict() for user in users])
        
        return jsonify({"message": "Nenhum usuário encontrado para esse cargo"}), 404
