from datetime import datetime, timezone
from app.repositories.document_repository import DocumentRepository
from .file_service import FileService
from app.models.document import Document
from app import db

UPLOAD_FOLDER = 'uploads/'

class DocumentService:
    def __init__(self):
        self.document_repo = DocumentRepository()
        self.file_service = FileService()

    def create_document(self, name, description,extension, folder_id, path, page_count):
        new_document = Document(
            name = name, 
            description = description, 
            extension = extension, 
            folder_id = folder_id, 
            path = path,
            page_count = page_count)

        self.document_repo.add(new_document)

        return new_document
    
    def get_document(self, document_id):
        return self.document_repo.get(document_id)
    
    def get_all_documents(self):
        return self.document_repo.get_all()
    
    def update_document(
            self, 
            document_id, 
            name = None, 
            description = None,
            extension = None,
            extracted_data = None,
            modified_data = None,
            folder_id = None,
            file = None,
            page_count = None
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
            document.path = self.file_service.update_file(file, document.name, document.path, UPLOAD_FOLDER)
            document.extension = extension
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
        if page_count:
            document.page_count = page_count

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