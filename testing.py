import os
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
    json.dump(mapping, f)
