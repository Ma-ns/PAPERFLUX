import os
import hashlib

class FileService:
    def upload_file(self, file, name, FOLDER):
        _, extension = os.path.splitext(file.filename)
        salt = os.urandom(16)
        filename_hash = hashlib.sha256(salt + name.replace(' ', '_').encode()).hexdigest()
        filename = f"{filename_hash}{extension}"
        path = os.path.join(FOLDER, filename)

        file.save(path)

        return path
    
    def update_file(self, file, name, path, FOLDER):
        os.remove(path)

        _, extension = os.path.splitext(file.filename)
        salt = os.urandom(16)
        filename_hash = hashlib.sha256(salt + name.replace(' ', '_').encode()).hexdigest()
        filename = f"{filename_hash}{extension}"
        path = os.path.join(FOLDER, filename)

        file.save(path)

        return path
    
    # adicionar delete file