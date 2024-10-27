from app import db

class Document(db.Model):
    __tablename__ = 'tb_ppf_document'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    path = db.Column(db.String(200), nullable=True)
    extracted_data = db.Column(db.JSON, nullable=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    
    folder_id = db.Column(db.Integer, db.ForeignKey('tb_ppf_folder.id'), nullable=True)

def __repr__(self):
        return f'<Document {self.name}>'