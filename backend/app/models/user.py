from app import db

class User(db.Model):
    __tablename__ = 'tb_ppf_user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    permissions = db.relationship('Permission', back_populates='user')

def __repr__(self):
        return f'<User {self.name}>'