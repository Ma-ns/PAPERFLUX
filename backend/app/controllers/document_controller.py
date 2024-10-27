import os
from flask import jsonify, request
from app.services.document_service import DocumentService

UPLOAD_FOLDER = 'uploads/'

class DocumentController:
    def __init__(self):
        self.document_service = DocumentService()

    def create_document(self):
        if 'file' not in request.files:
            return jsonify({"error": "Nenhum arquivo enviado"}), 400
        
        data = request.form
        file = request.files['file']

        name = data.get("name")
        description = data.get("description")

        if not name:
            return jsonify({"erro": "O nome é obrigatório!"}), 400
        
        _, extension = os.path.splitext(file.filename)
        filename = f"{name.replace(' ', '_')}{extension}"
        path = os.path.join(UPLOAD_FOLDER, filename)
        folder_id = data.get("folder_id")

        file.save(path)

        new_document = self.document_service.create_document(name, description, folder_id, path)

        return jsonify({
            "message": "Documento criado com sucesso!",
            "document": new_document.to_dict()
            }), 201

    def get_document(self, document_id):
        document = self.document_service.get_document(document_id)

        if document:
            return jsonify(document.to_dict())
        
        return jsonify({"message": "Documento não encontrado."}), 404

    def update_document(self, document_id):
        document = self.document_service.get_document(document_id)

        if not document:
            return jsonify({"message": "Documento não encontrado"}), 404
        
        data = request.form

        name = data.get("name")
        description = data.get("description")
        path = data.get("path")
        extracted_data = data.get("extracted_data")
        modified_data = data.get("modified_data")
        folder_id = data.get("folder_id")

        updated_document = self.document_service.update_document(document_id, name, description, path, extracted_data, modified_data, folder_id)

        if updated_document:
            return jsonify({
                "message": "Pasta atualizada com sucesso",
                "updated_document": updated_document.to_dict()
                }), 200
        return jsonify({"error": "O documento não pode ser atualizado"}), 404

    def delete_document(self, document_id):
        response = self.document_service.delete_document(document_id)

        if response:
            return jsonify({"message": "Documento excluído com sucesso"}), 200
        return jsonify({"message": "Documento não encontrado"}), 404