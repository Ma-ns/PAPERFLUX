from app import db

class Role(db.Model):
    __tablename__ = 'tb_ppf_role'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)

    users = db.relationship('User', back_populates='role')

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
        }

    def __repr__(self):
        return f'<Role {self.name}>'
