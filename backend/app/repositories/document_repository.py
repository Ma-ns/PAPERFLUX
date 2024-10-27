from app.models.document import Document
from .base_repository import BaseRepository

class DocumentRepository(BaseRepository):
    def __init__(self):
        super().__init__(Document)

    # Complementar
