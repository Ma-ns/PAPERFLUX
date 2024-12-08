from app.models.analysis import Analysis
from app.repositories.analysis_repository import AnalisysRepository

class AnalysisService:
    def __init__(self):
        self.repository = AnalisysRepository()

    def create_analysis(self, digitalized_documents, generated_residues, consult_economy, paper_use_by_role):
        new_analysis = Analysis(
            digitalized_documents = digitalized_documents,
            generated_residues = generated_residues,
            consult_economy = consult_economy,
            paper_use_by_role = paper_use_by_role
        )

        return self.repository.add(new_analysis)
    
    def get_analysis(self, id):
        return self.repository.get(id)
    
    def get_all_analysis(self):
        return self.repository.get_all()
    
    def update_analysis(
            self, 
            id, 
            digitalized_documents = None,
            generated_residues = None,
            consult_economy = None,
            paper_use_by_role = None
        ):

        analysis = self.repository.get(id)

        if digitalized_documents:
            analysis.digitalized_documents = digitalized_documents
        if generated_residues:
            analysis.generated_residues = generated_residues
        if consult_economy:
            analysis.consult_economy = consult_economy
        if paper_use_by_role:
            analysis.paper_use_by_role = paper_use_by_role
        
        return self.repository.update(id, analysis)
    
    def delete_analysis(self, id):
        return self.repository.delete(id)
    
    
