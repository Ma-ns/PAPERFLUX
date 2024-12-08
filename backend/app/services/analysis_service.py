from app.models.analysis import Analysis
from app.repositories.analysis_repository import AnalisysRepository
from app.repositories.document_repository import DocumentRepository
import pandas as pd
import numpy as np

class AnalysisService:
    def __init__(self):
        self.repository = AnalisysRepository()
        self.document_repository = DocumentRepository()

    def create_analysis(self, digitalized_documents, generated_residues, consult_economy, paper_use_by_role):
        new_analysis = Analysis(
            digitalized_documents = digitalized_documents,
            generated_residues = generated_residues,
            consult_economy = consult_economy,
            paper_use_by_role = paper_use_by_role
        )

        return self.repository.add(new_analysis)
    
    def get_analysis(self, id):
        analysis_data = self.repository.get_all()
        documents_data = self.document_repository.get_all()

        data = [analysis.to_dict() for analysis in analysis_data]
        df = pd.DataFrame(data)

        if documents_data:
            page_counts = [document['page_count'] for document in documents_data if 'page_count' in document]
            avg_page_count = np.mean(page_counts) if page_counts else 0

        df['avg_page_count'] = avg_page_count

        return df.to_dict(orient='records')
    
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
    
    
