import random

def select_random_entry(entries):
    if entries:
        return random.choice(entries)
    return None

def create_filter(property_name, filter_type, condition):
    return {
        "filter": {
            "property": property_name,
            filter_type: condition
        }
    }
