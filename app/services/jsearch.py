import requests
from app.config import Config


class JSearchService:
    BASE_URL = "https://jsearch.p.rapidapi.com"
    
    def __init__(self):
        self.headers = {
            "x-rapidapi-key": Config.RAPIDAPI_KEY,
            "x-rapidapi-host": Config.RAPIDAPI_HOST
        }
    
    def search_jobs(self, query, location=None, page=1, num_pages=1, 
                    date_posted="all", remote_jobs_only=False, 
                    employment_types=None):
        url = f"{self.BASE_URL}/search"
        
        params = {
            "query": query,
            "page": page,
            "num_pages": num_pages,
            "date_posted": date_posted,
            "remote_jobs_only": str(remote_jobs_only).lower()
        }
        
        if location:
            params["query"] = f"{query} in {location}"
        
        if employment_types:
            params["employment_types"] = employment_types
        
        try:
            response = requests.get(url, headers=self.headers, params=params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            return {"error": str(e), "data": []}
    
    def get_job_details(self, job_id):
        url = f"{self.BASE_URL}/job-details"
        
        params = {"job_id": job_id}
        
        try:
            response = requests.get(url, headers=self.headers, params=params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            return {"error": str(e), "data": []}
    
    def get_estimated_salary(self, job_title, location, radius=100):
        url = f"{self.BASE_URL}/estimated-salary"
        
        params = {
            "job_title": job_title,
            "location": location,
            "radius": radius
        }
        
        try:
            response = requests.get(url, headers=self.headers, params=params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            return {"error": str(e), "data": []}
