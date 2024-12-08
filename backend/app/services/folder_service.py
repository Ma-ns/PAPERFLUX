from app.repositories.folder_repository import FolderRepository
from app.models.folder import Folder
from app import db

class FolderService:
    def __init__(self):
        self.folder_repo = FolderRepository()

    def create_folder(self, name, description):
        new_folder = Folder(name = name, description = description)

        self.folder_repo.add(new_folder)

        return new_folder
    
    def get_folder(self, folder_id):
        return self.folder_repo.get(folder_id)
    
    def get_all_folders(self):
        return self.folder_repo.get_all()

    def update_folder(self, folder_id, name = None, description = None):
        folder = self.folder_repo.get(folder_id)
        if not folder:
            return None
        
        if name:
            folder.name = name

        if description:
            folder.description = description

        self.folder_repo.update(folder)

        return folder
    
    def delete_folder(self, folder_id):
        folder = self.folder_repo.get(folder_id)

        if folder:
            self.folder_repo.delete(folder)
            return True
        
        return False
    
    def get_all_documents(self, folder_id):
        return self.folder_repo.get_all_documents(folder_id)