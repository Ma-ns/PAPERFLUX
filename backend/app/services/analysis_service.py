from repositories.document_repository import DocumentRepository

class AnalysisService:
    @staticmethod
    def get_analysis_data():
        sustainability_data = SustainabilityRepository.fetch_data()
        warm_data = WarmRepository.fetch_data()
        carbon_data = CarbonRepository.fetch_data(1000)

        df_sustainability = pd.DataFrame(sustainability_data["data"])
        df_warm = pd.DataFrame(warm_data["results"])
        df_carbon = pd.DataFrame(carbon_data)

        df_combined = pd.concat([df_sustainability, df_warm, df_carbon], axis=1)
        return df_combined
    
    def calculate_printing_cost(self, total_pages, cost_per_page):
        total_cost = total_pages * cost_per_page
        return total_cost
    
    def calculate_weight_in_grams(self, total_pages, weight_per_page):
        total_weight = total_pages * weight_per_page
        return total_weight
    
    @staticmethod
    def get_summaryPannel_data():
        total_pages = DocumentRepository.get_total_pages()

        printing_economy = AnalysisService.calculate_printing_cost(total_pages, 1.5)
        total_weight = AnalysisService.calculate_weight_in_grams(total_pages, 50)

        return {
            "total_pages": total_pages,
            "printing_economy": printing_economy,
            "total_weight": total_weight
        }
    
    
