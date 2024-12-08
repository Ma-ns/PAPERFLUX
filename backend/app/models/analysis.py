from app import db

class Analysis(db.Model):
    __tablename__ = 'tb_ppf_analysis'

    id = db.Column(db.Integer, primary_key=True)
    digitalized_documents = db.Column(db.Integer, default=0)
    generated_residues = db.Column(db.Integer, default=0)
    consult_economy = db.Column(db.String(200), nullable=True)
    paper_use_by_role = db.Column(db.JSON, nullable=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    def to_dict(self):
        return{
            'id': self.id,
            'digitalized_documents': self.digitalized_documents,
            'generated_residues': self.generated_residues,
            'consult_economy': self.consult_economy,
            'paper_use_by_role': self.paper_use_by_role
        }

def __repr__(self):
        return f'<Analysis {self.name}>'