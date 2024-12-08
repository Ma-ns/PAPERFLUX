from app import db
from app.models.analysis import Analysis
from .base_repository import BaseRepository

class AnalisysRepository(BaseRepository):
    def __init__(self):
        super().__init__(Analysis)
