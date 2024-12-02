import requests

class SustainabilityRepository:
    API_URL = "https://api.opensustainability.org/v1/resources/paper"
    HEADERS = {"Authorization": "Bearer YOUR_API_KEY"}

    @staticmethod
    def fetch_data():
        response = requests.get(SustainabilityRepository.API_URL, headers=SustainabilityRepository.HEADERS)

        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()