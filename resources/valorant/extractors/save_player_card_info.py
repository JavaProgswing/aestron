import requests
import json

api_url_playercards = "https://valorant-api.com/v1/playercards"
json_file_path_playercards = "player_card_info.json"

try:
    # Fetch data from the player cards API
    response_playercards = requests.get(api_url_playercards)

    # Check if the request was successful (status code 200)
    if response_playercards.status_code == 200:
        # Parse JSON response for player cards
        playercards_data = response_playercards.json()

        # Save data to a JSON file for player cards
        with open(json_file_path_playercards, 'w', encoding='utf-8') as json_file_playercards:
            json.dump(playercards_data, json_file_playercards, ensure_ascii=False, indent=4)
        
        print(f"Player card data successfully fetched and saved to {json_file_path_playercards}")
    else:
        print(f"Failed to fetch player card data. Status code: {response_playercards.status_code}")

except Exception as e:
    print(f"An error occurred while fetching player card data: {e}")
