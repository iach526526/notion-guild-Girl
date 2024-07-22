import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Environment variables
token = os.getenv('Notion-token')
database_id = os.getenv('Database-id')

# Headers for the Notion API requests
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

def query_database(filter_json):
    response = requests.post(
        f"https://api.notion.com/v1/databases/{database_id}/query",
        headers=headers,
        json=filter_json
    )
    print(response.json())
    return response.json()["results"]

def update_entry(entry_id, new_tag):
    response = requests.patch(
        f"https://api.notion.com/v1/pages/{entry_id}",
        headers=headers,
        json={
            "properties": {
                "優先順序": {
                    "select": {"name": new_tag}
                }
            }
        }
    )
    return response.json()
