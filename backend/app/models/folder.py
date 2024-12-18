from app import db

class Folder(db.Model):
    __tablename__ = 'tb_ppf_folder'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=True)
    private = db.Column(db.Boolean, default=False)

    role_id = db.Column(db.Integer, db.ForeignKey('tb_ppf_role.id'), nullable=True)

    documentos = db.relationship('Document', backref = 'Folder', lazy=True)

    def to_dict(self):
        return{
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "private": self.private
        }

def __repr__(self):
        return f'<Folder {self.name}>'