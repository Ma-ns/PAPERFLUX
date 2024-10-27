from flask import jsonify, request
from app.services.folder_service import FolderService

class FolderController:
    def __init__(self):
        self.folder_service = FolderService()

    def create_folder(self): #Criação de nova pasta
        data = request.get_json()

        name = data.get("name")
        description = data.get("description")

        if not name:
            return jsonify({"error": "O nome é obrigatório"}), 400
        
        new_folder = self.folder_service.create_folder(name, description)

        return jsonify({
            "message": "Pasta criada com sucesso!",
            "folder": new_folder.to_dict()
            }), 201
    
    def get_folder(self, folder_id):
        folder = self.folder_service.get_folder(folder_id)

        if folder:
            return jsonify(folder.to_dict())
        
        return jsonify({"message": "Pasta não encontrada."}), 404

    def update_folder(self, folder_id):
        folder = self.folder_service.get_folder(folder_id)

        if not folder:
            return jsonify({"message": "Pasta não encontrada"}), 404
        
        data = request.get_json()

        name = data.get("name")
        description = data.get("description")

        updated_folder = self.folder_service.update_folder(folder_id, name, description)

        if updated_folder:
            return jsonify({
                "message": "Pasta atualizada com sucesso",
                "updated_folder": updated_folder.to_dict()
                }), 200
        return jsonify({"error": "A pasta não pode ser atualizada"}), 404

    def delete_folder(self, folder_id):
        response = self.folder_service.delete_folder(folder_id)

        if response:
            return jsonify({"message": "Pasta excluída com sucesso"}), 200
        return jsonify({"message": "Pasta não encontrada"}), 404