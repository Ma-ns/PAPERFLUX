from app import db

class Analysis(db.Model):
    __tablename__ = 'tb_ppf_analysis'

    id = db.Column(db.Integer, primary_key=True)
    digitalized_documents = db.Column(db.Integer, default=0)
    generated_residues = db.Column(db.Integer, default=0)

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
        return f'<Analysis {self.name}>'