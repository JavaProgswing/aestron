import requests
import json

api_url_weapons = "https://valorant-api.com/v1/weapons"
json_file_path_weapons = "weapon_info.json"

try:
    # Fetch data from the weapons API
    response_weapons = requests.get(api_url_weapons)

    # Check if the request was successful (status code 200)
    if response_weapons.status_code == 200:
        # Parse JSON response for weapons
        weapons_data = response_weapons.json()

        # Save data to a JSON file for weapons
        with open(json_file_path_weapons, 'w', encoding='utf-8') as json_file_weapons:
            json.dump(weapons_data, json_file_weapons, ensure_ascii=False, indent=4)
        
        print(f"Weapon data successfully fetched and saved to {json_file_path_weapons}")
    else:
        print(f"Failed to fetch weapon data. Status code: {response_weapons.status_code}")

except Exception as e:
    print(f"An error occurred while fetching weapon data: {e}")
