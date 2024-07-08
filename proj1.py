import os

def get_file_info():
    files = os.listdir('.')
    file_info_list = []

    for file in files:
        if os.path.isfile(file):
            file_info = {
                'name': file,
                'size': os.path.getsize(file)
            }
            file_info_list.append(file_info)

    return file_info_list

if __name__ == "__main__":
    file_info_list = get_file_info()
    for file_info in file_info_list:
        print(f"File Name: {file_info['name']}, File Size: {file_info['size']} bytes")
