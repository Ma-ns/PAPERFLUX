from app import db
from app.models.document import Document
from .base_repository import BaseRepository

class DocumentRepository(BaseRepository):
    def __init__(self):
        super().__init__(Document)

    def get_total_pages(self):
        total_pages = db.session.query(db.func.sum(Document.page_count)).scalar()
        return total_pages or 0
