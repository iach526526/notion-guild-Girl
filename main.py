import os
import requests
import json
import random
from dotenv import load_dotenv

# Load environment variables
load_dotenv(f'{os.getcwd()}/.env')
token = os.getenv('Notion-token')
database_id = os.getenv('Database-id')

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
    data = response.json()
    return data["results"]

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
if __name__ == "__main__":
    # Step 1: Reset priority for entries with "🔥今日重點" and "Done?" unchecked
    reset_filter = {
        "filter": {
            "and": [
                {
                    "property": "優先順序",
                    "select": {"equals": "🔥今日重點"}
                },
                {
                    "property": "Done?",
                    "checkbox": {"equals": False}
                }
            ]
        }
    }
    reset_entries = query_database(reset_filter)

    for entry in reset_entries:
        update_entry(entry["id"], "等待")

    # Step 2: Fetch entries with "🎲random" tag and select a random one
    random_filter = {
        "filter": {
            "property": "情境",
            "multi_select": {"contains": "🎲random"}
        }
    }
    entries = query_database(random_filter)

    # Select a random entry and update its priority to "🔥今日重點"
    if entries:
        selected_entry = random.choice(entries)
        entry_id = selected_entry["id"]
        update_response = update_entry(entry_id, "🔥今日重點")
        print(update_response)
    else:
        print("No entries found with the 'random' tag")