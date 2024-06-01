def write_file(file_name, file_content):
    # We start by opening the file while appending the .txt suffix
    # We then tell it to write it to the file. this "file" can have any name tbh. e.g. in the next example i'll call it text_file
    with open(f"{file_name}.txt", mode="w", encoding="utf-8") as file:
        file.write(file_content)

def append_file(file_name, append_content):
    with open(f"{file_name}.txt", mode="a", encoding="utf-8") as text_file:
        text_file.write(append_content)

def read_file(file_name):
    with open(f"{file_name}.txt",mode="r", encoding="utf-8") as text_file:
        # We create a variable to hold the data to be read
        content = text_file.read()
        return content

# Alternatively
'''def read_file(file_name):
    #Add the .txt extension
    #Open file in read mode and return the content
    with open(f'{file_name}.txt', 'r') as file:
        return file.read()'''