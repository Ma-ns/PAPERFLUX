from app import db

class Permission(db.Model):
    __tablename__ = 'tb_ppf_permission'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('tb_ppf_user.id'), nullable=False)
    folder_id = db.Column(db.Integer, db.ForeignKey('tb_ppf_folder.id'), nullable=False)

    user = db.relationship('User', back_populates='permissions')
    folder = db.relationship('Folder')

    id = db.Column(db.Integer, primary_key = True)

    def __repr__(self):
        return f'<Permission User {self.user_id} Folder {self.folder_id}>'
    