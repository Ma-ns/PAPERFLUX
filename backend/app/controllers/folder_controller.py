from flask import jsonify, request
from app.repositories.folder_repository import FolderRepository
from app.models.folder import Folder
from app import db

class FolderController:
    def __init__(self):
        self.folder_repo = FolderRepository()

    def create_folder(self): #Criação de nova pasta
        data = request.get_json()

        name = data.get("name")
        description = data.get("description")

        new_folder = Folder(name = name, description = description)

        self.folder_repo.add(new_folder)

        return jsonify({"message": "Pasta criada com sucesso!"}), 201
    
    def get_folder(self, folder_id):
        folder = self.folder_repo.get(folder_id)

        if folder:
            return jsonify({
                "id": folder.id,
                "name": folder.name,
                "description": folder.description
            })
        
        return jsonify({"message": "Pasta não encontrada."}), 404

    def update_folder(self, folder_id):
        folder = self.folder_repo.get(folder_id)

        if not folder:
            return jsonify({"message": "Pasta não encontrada"}), 404
        
        data = request.get_json()

        folder.name = data.get("name", folder.name)
        folder.description = data.get("description", folder.description)

        self.folder_repo.update()

        return jsonify({"message": "Pasta atualizada com sucesso"}), 200


    def delete_folder(self, folder_id):
        folder = self.folder_repo.get(folder_id)

        if not folder:
            return jsonify({"message": "Pasta não encontrada"}), 404
        
        self.folder_repo.delete(folder)

        return jsonify({"message": "Pasta excluída com sucesso"}), 200