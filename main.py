import os
import requests
import json
import random
from dotenv import load_dotenv
load_dotenv(f'{os.getcwd()}/.env')
token = os.getenv('Notion-token')
database_id = os.getenv('Database-id')

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

def get_database_entries(database_id):
    response = requests.post(
        f"https://api.notion.com/v1/databases/{database_id}/query",
        headers=headers,
        json={
            "filter": {
                "property": "情境",
                "multi_select": {
                    "contains": "🎲random"
                }
            }
        }
    )
    data = response.json()
    with open("res.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    return data["results"]

def update_entry(entry_id, new_tag):
    #把優先順序的欄位標記為今日重點
    response = requests.patch(
        f"https://api.notion.com/v1/pages/{entry_id}",
        headers=headers,
        json={
            "properties": {
                "優先順序": {
                    "select": 
                        {"name": new_tag}
                }
            }
        }
    )
    return response.json()

# Fetch entries
entries = get_database_entries(database_id)

# Select a random entry
if entries:
    selected_entry = random.choice(entries)
    entry_id = selected_entry["id"]

    # Update the entry with "今日重點" tag
    update_response = update_entry(entry_id, "🔥今日重點")
    # print(update_response)
else:
    print("No entries found with the 'random' tag")