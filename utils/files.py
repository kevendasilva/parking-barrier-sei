import os

def file_exists(filename, path):
    file_path = os.path.join(path, filename)

    if not os.path.isfile(file_path):
        print(f"File '{filename}' not found in path '{path}'.")
        return False
    
    return True


def read_file(filename, path):
    try:
        file_path = os.path.join(path, filename)
        with open(file_path, 'r') as file:
            content = file.read().strip()
            return content

    except FileNotFoundError:
        print(f"File '{filename}' not found in path '{path}'.")
        return None

    except Exception as e:
        print(f"An error occurred while reading the file '{filename}' at path '{path}': {str(e)}")
        return None
