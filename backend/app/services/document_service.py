import os
from app.repositories.document_repository import DocumentRepository
from app.models.document import Document
from app import db
from datetime import datetime, timezone

UPLOAD_FOLDER = 'uploads/'

class DocumentService:
    def __init__(self):
        self.document_repo = DocumentRepository()

    def upload_file(self, file, name):
        _, extension = os.path.splitext(file.filename)
        filename = f"{name.replace(' ', '_')}{extension}"
        path = os.path.join(UPLOAD_FOLDER, filename)

        file.save(path)

        return path
    
    def update_file(self, file, name, path):
        os.remove(path)

        _, extension = os.path.splitext(file.filename)
        filename = f"{name.replace(' ', '_')}{extension}"
        path = os.path.join(UPLOAD_FOLDER, filename)

        file.save(path)

        return path

    def create_document(self, name, description, folder_id, path):
        new_document = Document(name = name, description = description, folder_id = folder_id, path = path)

        self.document_repo.add(new_document)

        return new_document
    
    def get_document(self, document_id):
        return self.document_repo.get(document_id)
    
    def update_document(
            self, 
            document_id, 
            name = None, 
            description = None,
            extracted_data = None,
            modified_data = None,
            folder_id = None,
            file = None
            ):
        
        document = self.document_repo.get(document_id)

        if not document:
            return None
        
        modified = False

        if name and name != document.name:
            document.name = name
            modified = True
        if description and description != document.description:
            document.description = description
            modified = True
        if file: 
            document.path = self.update_file(file, document.name, document.path)
            document.extracted_data = None
            document.modified_data = None
            
            modified = True
        if extracted_data and not document.extracted_data:
            document.extracted_data = extracted_data
            modified = True
        if modified_data and modified_data != document.modified_data:
            document.modified_data = modified_data
            modified = True
        if folder_id:
            document.folder_id = folder_id

        if modified:
            document.modified_at = datetime.now(timezone.utc)

        self.document_repo.update(document)

        return document
    
    def delete_document(self, document_id):
        document = self.document_repo.get(document_id)

        if document:
            self.document_repo.delete(document)
            return True
        
        return False