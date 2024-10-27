from flask import jsonify, request
from backend.app.repositories.document_repository import DocumentRepository
from app.models.document import Document
from app import db

class DocumentController:
    def __init__(self):
        self.document_repo = DocumentRepository()

    def create_document(self):
        data = request.get_json()

        name = data.get("name")
        description = data.get("description")
        folder_id = data.get("folder_id")

        new_document = Document(name = name, description = description, folder_id = folder_id)

        self.document_repo.add(new_document)

        return jsonify({"message": "Documento criado com sucesso!"}), 201

    def get_document(self, document_id):
        document = self.document_repo.get(document_id)

        if document:
            return jsonify({
                "id": document.id,
                "name": document.name,
                "description": document.description,
                "path": document.path,
                "extracted_data": document.extracted_data,
                "created_at": document.created_at,
                "folder_id": document.folder_id
            })
        
        return jsonify({"message": "Documento não encontrado."}), 404

    def update_document(self, document_id):
        document = self.document_repo.get(document_id)

        if not document:
            return jsonify({"message": "Documento não encontrado"}), 404
        
        data = request.get_json()

        document.name = data.get("name", document.name)
        document.description = data.get("description", document.description)
        document.path = data.get("path", document.path)
        document.extracted_data = data.get("extracted_data", document.extracted_data)
        document.folder_id = data.get("folder_id", document.folder_id)

        self.document_repo.update()

        return jsonify({"message": "Pasta atualizada com sucesso"}), 200

    def delete_document(self, document_id):
        document = self.document_repo.get(document_id)

        if not document:
            return jsonify({"message": "Documento não encontrado"}), 404
        
        self.document_repo.delete(document)

        return jsonify({"message": "Documento excluído com sucesso"}), 200