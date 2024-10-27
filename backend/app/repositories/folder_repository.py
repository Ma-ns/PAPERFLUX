from app.models.folder import Folder
from app.models.document import Document
from .base_repository import BaseRepository

class FolderRepository(BaseRepository):
    def __init__(self):
        super().__init__(Folder)

    def get_all_documents(self, folder_id):
        return Document.query.filter_by(folder_id = folder_id).all()