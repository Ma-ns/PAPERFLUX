from app import db

class BaseRepository:
    def __init__(self, model):
        self.model = model

    def add(self, entity):
        db.session.add(entity)
        db.session.commit()

    def get(self, entity_id):
        return self.model.query.get(entity_id)
    
    def update(self, entity):
        db.session.delete(entity)
        db.session.commit()

    def get_all(self):
        return self.model.query.all()