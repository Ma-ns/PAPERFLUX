from flask import Blueprint
from app.controllers.folder_controller import FolderController
from app.controllers.document_controller import DocumentController
from app.controllers.user_controller import UserController
from app.controllers.permission_controller import PermissionController

folder_controller = FolderController()
document_controller = DocumentController()
user_controller = UserController()
permission_controller = PermissionController()

routes = Blueprint('routes', __name__)

# Rotas para Pasta
routes.route('/folder', methods=['POST'])(folder_controller.create_folder)
routes.route('/folder/<int:folder_id>', methods=['GET'])(folder_controller.get_folder)
routes.route('/folder/<int:folder_id>/documents', methods=['GET'])(folder_controller.get_all_documents)
routes.route('/folder/<int:folder_id>', methods=['PUT'])(folder_controller.update_folder)
routes.route('/folder/<int:folder_id>', methods=['DELETE'])(folder_controller.delete_folder)

# Rotas para Documento
routes.route('/document', methods=['POST'])(document_controller.create_document)
routes.route('/document/<int:document_id>', methods=['GET'])(document_controller.get_document)
routes.route('/document/<int:document_id>', methods=['PUT'])(document_controller.update_document)
routes.route('/document/<int:document_id>', methods=['DELETE'])(document_controller.delete_document)

# Rotas para Usuário
routes.route('/user', methods=['POST'])(user_controller.create_user)
routes.route('/user/<int:user_id>', methods=['GET'])(user_controller.get_user)
routes.route('/user/<int:user_id>', methods=['PUT'])(user_controller.update_user)
routes.route('/user/<int:user_id>/profile_pic', methods=['PUT'])(user_controller.update_profilePic)
routes.route('/user/<int:user_id>', methods=['DELETE'])(user_controller.delete_user)
routes.route('/user/validate_login', methods=['GET'])(user_controller.validate_login)

# Rotas para Permissão
routes.route('/permission', methods=['POST'])(permission_controller.assign_permission)
routes.route('/permission', methods=['DELETE'])(permission_controller.undesignate_permission)