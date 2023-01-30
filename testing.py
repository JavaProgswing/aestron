"""import os
import json

folder_path = 'C:\\Users\\HP\\Videos'
input_folder_path= os.path.join(folder_path, 'input')
output_folder_path= os.path.join(folder_path, 'output')
mapping = {}

for file_name in os.listdir(input_folder_path):
    if file_name.endswith('.mkv'):
        original_file = os.path.join(input_folder_path, file_name)
        new_file = os.path.join(output_folder_path, file_name.replace('.mkv', '.gif'))
        os.system(
            f'ffmpeg -i {original_file} -vf "fps=15,scale=-1:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" -b:v 1M {new_file}')
        mapping[original_file] = new_file

with open(os.path.join(output_folder_path, 'mapping.json'), 'w') as f:
    json.dump(mapping, f)"""
import os
import requests
from dotenv import load_dotenv
load_dotenv(dotenv_path="github.env")
def compare_local_remote_git_repo(files):
    GITHUB_OWNER = os.getenv("GITHUB_OWNER")
    GITHUB_REPO = os.getenv("GITHUB_REPO")

    for filename in files:
        # Get the content of the file from the remote repository
        print(f"Comparing {filename}...")
        file_url = f"https://requestsforward.webdashboard.repl.co/redirect?url=https://api.github.com/repos/{GITHUB_OWNER}/{GITHUB_REPO}/contents/{filename}"
        print(file_url)
        file_response = requests.get(file_url, headers={"Authorization": f"Bearer {os.getenv('GITHUB_TOKEN')}", "Accept": "application/vnd.github+json", "X-GitHub-Api-Version": "2022-11-28"})
        if(file_response.status_code==404):
            print(f"{filename} is not present in the remote repository.")
            continue
        parsed_file_response = file_response.json()
        print(parsed_file_response)
        try:
            remote_file_content = parsed_file_response["content"]
        except KeyError:
            print(f"{filename} doesn't have a content!?")
            continue
        # Get the content of the file from the local repository
        with open(filename, "r", encoding="utf8") as file:
            local_file_content = file.read()

        # Compare the two file contents
        if remote_file_content != local_file_content:
            print(f"{filename} differs from the remote version.")
    print("Comparison complete.")


files = ["testing.py","main.py"]
compare_local_remote_git_repo(files)