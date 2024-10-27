from app import db

class Folder(db.Model):
    __tablename__ = 'tb_ppf_folder'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=True)

    documentos = db.relationship('Document', backref = 'Folder', lazy=True)

def __repr__(self):
        return f'<Folder {self.name}>'