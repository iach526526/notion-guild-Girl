from notion_api import query_database, update_entry
from utils import select_random_entry, create_filter
if __name__ == "__main__":
    # Step 1: Reset priority for entries with "🔥今日重點" and "Done?" unchecked
    #把情境包含"🔥今日重點"標籤且"Done?"未勾選的條目重置為"等待"(這些就是昨天沒做完的啦)
    reset_filter = create_filter("優先順序", "select", {"equals": "🔥今日重點"})
    done_filter = create_filter("Done?", "checkbox", {"equals": False})

    reset_entries = query_database({
        "filter": {
            "and": [reset_filter["filter"], done_filter["filter"]]
        }
    })

    for entry in reset_entries:
        update_entry(entry["id"], "等待")

    # Step 2: Fetch entries with "🎲random" tag and  and "Done?" unchecked
    #把情境包含"🎲random"標籤的條目且"Done?"未勾選的條目抓取出來
    random_filter = create_filter("情境", "multi_select", {"contains": "🎲random"})
    random_done_filter = create_filter("Done?", "checkbox", {"equals": False})

    entries = query_database({
        "filter": {
            "and": [random_filter["filter"], random_done_filter["filter"]]
        }
    })


    # Select a random entry and update its priority to "🔥今日重點"
    #隨機選擇一個條目並將其優先順序更新為"🔥今日重點"
    selected_entry = select_random_entry(entries)
    if selected_entry:
        entry_id = selected_entry["id"]
        update_response = update_entry(entry_id, "🔥今日重點")
    else:
        print("No entries found with the 'random' tag")
