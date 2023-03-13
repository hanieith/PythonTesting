def read_from_file(file_path):
    with open(file_path, 'r') as file_object:
        return file_object.readlines()
