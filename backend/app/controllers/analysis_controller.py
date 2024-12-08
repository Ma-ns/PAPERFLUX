import os
from flask import jsonify, request
from app.services.analysis_service import AnalysisService

class AnalysisController:
    def __init__(self):
        self.analysis_service = AnalysisService()

    def create_analysis(self):       
        data = request.form

        digitalized_documents = data.get("digitalized_documents")
        generated_residues = data.get("generated_residues")
        consult_economy = data.get("consult_economy")
        paper_use_by_role = data.get("paper_use_by_role")

        new_analysis = self.analysis_service.create_analysis(
            digitalized_documents, 
            generated_residues, 
            consult_economy, 
            paper_use_by_role
        )

        return jsonify({
            "message": "Documento criado com sucesso!",
            "document": new_analysis.to_dict()
            }), 201

    def get_analysis(self, analysis_id):
        analysis = self.get_analysis(analysis_id)

        if analysis:
            return jsonify(analysis.to_dict())
        
        return jsonify({"message": "Análise não encontrada."}), 404

    def update_analysis(self, analysis_id):
        analysis = self.analysis_service.get_analysis(analysis_id)

        if not analysis:
            return jsonify({"message": "Análise não encontrada"}), 404
        
        data = request.form

        digitalized_documents = data.get("digitalized_documents")
        generated_residues = data.get("generated_residues")
        consult_economy = data.get("consult_economy")
        paper_use_by_role = data.get("paper_use_by_role")

        updated_analysis = self.analysis_service.update_analysis(
            analysis_id,
            digitalized_documents,
            generated_residues,
            consult_economy,
            paper_use_by_role
        )

        if updated_analysis:
            return jsonify({
                "message": "Análise atualizada com sucesso",
                "updated_document": updated_analysis.to_dict()
                }), 200
        return jsonify({"error": "A análise não pode ser atualizada"}), 404

    def delete_analysis(self, analysis_id):
        response = self.analysis_service.delete_analysis(analysis_id)

        if response:
            return jsonify({"message": "Análise excluída com sucesso"}), 200
        return jsonify({"message": "Análise não encontrada"}), 404