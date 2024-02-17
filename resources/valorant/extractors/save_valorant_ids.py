import requests
import json
import os
from dotenv import load_dotenv

# Load environment variables from .env file
dotenv_path = "C:\\Users\\yasha\\Documents\\aestron\\.env"  # Adjust the path based on your directory structure
load_dotenv(dotenv_path)

# Define API endpoint and file paths
api_url_contents = "https://ap.api.riotgames.com/val/content/v1/contents"
json_file_path_ids = 'valorant_ids.json'

try:
    # Get VAL_API_TOKEN from environment variables
    api_key = os.getenv("VAL_API_TOKEN")
    if not api_key:
        raise ValueError("VAL_API_TOKEN not found in the .env file.")

    # Set up query parameters
    params = {
        'locale': 'en-US',
        'api_key': api_key
    }

    # Fetch data from the Riot Games API
    response_contents = requests.get(api_url_contents, params=params)

    # Check if the request was successful (status code 200)
    if response_contents.status_code == 200:
        # Parse JSON response for content IDs
        content_ids_data = response_contents.json()

        # Save data to a JSON file for content IDs
        with open(json_file_path_ids, 'w', encoding='utf-8') as json_file_ids:
            json.dump(content_ids_data, json_file_ids, ensure_ascii=False, indent=4)

        print(f"Valorant content IDs successfully fetched and saved to {json_file_path_ids}")
    else:
        print(f"Failed to fetch Valorant content IDs. Status code: {response_contents.status_code}")

except Exception as e:
    print(f"An error occurred while fetching Valorant content IDs: {e}")
