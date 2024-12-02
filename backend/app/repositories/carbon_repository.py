import requests

class CarbonRepository:
    API_URL = "https://api.carboninterface.com/v1/estimates"
    HEADERS = {"Authorization": "Bearer YOUR_API_KEY"}

    @staticmethod
    def fetch_data(paper_usage):
        payload = {"type": "paper", "usage": paper_usage}
        response = requests.get(CarbonRepository.API_URL, headers=CarbonRepository.HEADERS, json=payload)

        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()