from flask import Blueprint
from app.controllers.folder_controller import FolderController
from app.controllers.document_controller import DocumentController

folder_controller = FolderController()
document_controller = DocumentController()

routes = Blueprint('routes', __name__)

# Rotas para Pasta
routes.route('/folder', methods=['POST'])(folder_controller.create_folder)
routes.route('/folder/<int:folder_id>', methods=['GET'])(folder_controller.get_folder)
routes.route('/folder/<int:folder_id>', methods=['PUT'])(folder_controller.update_folder)
routes.route('/folder/<int:folder_id>', methods=['DELETE'])(folder_controller.delete_folder)

# Rotas para Documento
routes.route('/document', methods=['POST'])(document_controller.create_document)
routes.route('/document/<int:document_id>', methods=['GET'])(document_controller.get_document)
routes.route('/document/<int:document_id>', methods=['PUT'])(document_controller.update_document)
routes.route('/document/<int:document_id>', methods=['DELETE'])(document_controller.delete_document)
