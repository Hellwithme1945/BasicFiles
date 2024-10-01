import os

directory = r"C:\Users\firer\Downloads"

filenames = ["1.txt", "2.txt", "3.txt"]

files_info = []

for filename in filenames:
    filepath = os.path.join(directory, filename)
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.readlines()
        num_lines = len(content)
        files_info.append({
            'name': filename,
            'num_lines': num_lines,
            'content': content
        })

files_info.sort(key=lambda x: x['num_lines'])

output_path = os.path.join(directory, 'result.txt')
with open(output_path, 'w', encoding='utf-8') as outfile:
    for file in files_info:

        outfile.write(f"{file['name']}\n")
        outfile.write(f"{file['num_lines']}\n")

        outfile.writelines(file['content'])
