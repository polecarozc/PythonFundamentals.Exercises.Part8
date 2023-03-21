import os

file_path = '/Users/jacobp/Desktop/projects/WEEK3/PythonFundamentals.Exercises.Part8'

def director_reader(path_name):
    path = ""
    for file in os.listdir(path_name):
        path += os.path.join(path_name, file) + "\n"
    return path

def writing_file(text):
    with open('directory_list.txt', 'w') as file:
        file.write(str(text))


writing_file(director_reader(file_path))