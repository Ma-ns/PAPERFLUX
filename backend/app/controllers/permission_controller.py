from flask import jsonify, request
from app.services.permission_service import PermissionService

class PermissionController:
    def __init__(self):
        self.permission_service = PermissionService()

    def assign_permission(self): #Criação de nova pasta
        data = request.get_json()

        user_id = data.get("user_id")
        folder_id = data.get("folder_id")

        if not user_id or not folder_id:
            return jsonify({"error": "Dados incompletos"}), 400
        
        new_permission = self.permission_service.assign_permission(user_id, folder_id)

        if new_permission:
            return jsonify({
                "message": "Permissão atribuida com sucesso!"}), 201
        return jsonify({"message": "Não foi possível atribuir a permissão."})
    
    def undesignate_permission(self):
        data = request.get_json()

        user_id = data.get("user_id") 
        folder_id = data.get("folder_id")

        if not user_id or not folder_id:
            return jsonify({"error": "Dados incompletos"}), 400
        
        response = self.permission_service.undesignate_permission(user_id, folder_id)

        if response:
            return jsonify({"message": "Permissão retirada com sucesso"})
        return jsonify({"message": "Não foi possível retirar a permissão"})
        

    