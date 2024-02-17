import requests
import json

api_url = "https://valorant-api.com/v1/agents?isPlayableCharacter=true"
json_file_path = "agent_info.json"

try:
    # Fetch data from the API
    response = requests.get(api_url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse JSON response
        agent_data = response.json()

        # Save data to a JSON file
        with open(json_file_path, 'w', encoding='utf-8') as json_file:
            json.dump(agent_data, json_file, ensure_ascii=False, indent=4)
        
        print(f"Data successfully fetched and saved to {json_file_path}")
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")

except Exception as e:
    print(f"An error occurred: {e}")
