from app import db

class Document(db.Model):
    __tablename__ = 'tb_ppf_document'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    extension = db.Column(db.String(50), nullable=False)
    path = db.Column(db.String(200), nullable=True)
    extracted_data = db.Column(db.JSON, nullable=True)
    page_count = db.Column(db.Integer, default=1)
    modified_data = db.Column(db.JSON, nullable=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    modified_at = db.Column(db.DateTime, nullable=True)
    consults = db.Column(db.Integer, default=0)
    
    folder_id = db.Column(db.Integer, db.ForeignKey('tb_ppf_folder.id'), nullable=True)

    def to_dict(self):
        return{
            "document_id": self.id,
            "name": self.name,
            "description": self.description,
            "extension": self.extension,
            "path": self.path,
            "extracted_data": self.extracted_data,
            "page_count": self.page_count,
            "modified_data": self.modified_data,
            "created_at": self.created_at,
            "modified_at": self.modified_at,
            "folder_id": self.folder_id
        }

def __repr__(self):
        return f'<Document {self.name}>'