import requests
import json

api_url_maps = "https://valorant-api.com/v1/maps"
json_file_path_maps = "map_info.json"

try:
    # Fetch data from the maps API
    response_maps = requests.get(api_url_maps)

    # Check if the request was successful (status code 200)
    if response_maps.status_code == 200:
        # Parse JSON response for maps
        map_data = response_maps.json()

        # Save data to a JSON file for maps
        with open(json_file_path_maps, 'w', encoding='utf-8') as json_file_maps:
            json.dump(map_data, json_file_maps, ensure_ascii=False, indent=4)
        
        print(f"Map data successfully fetched and saved to {json_file_path_maps}")
    else:
        print(f"Failed to fetch map data. Status code: {response_maps.status_code}")

except Exception as e:
    print(f"An error occurred while fetching map data: {e}")
