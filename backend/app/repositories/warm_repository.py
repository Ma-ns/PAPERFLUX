import requests

class WarmRepository:
    API_URL = "https://api.epa.gov/warm/v1/paper-usage"
    HEADERS = {"Authorization": "Bearer YOUR_API_KEY"}

    @staticmethod
    def fetch_data():
        response = requests.get(WarmRepository.API_URL, headers=WarmRepository.HEADERS)

        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()