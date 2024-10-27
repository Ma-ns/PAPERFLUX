from app.models.folder import Folder
from .base_repository import BaseRepository

class FolderRepository(BaseRepository):
    def __init__(self):
        super().__init__(Folder)

    # Complementar