import os

def test_write_to_text_file():

    file_path = os.path.join(os.getcwd(), "data/test.txt")
    with open(file_path, 'w') as file:
        file.write("ho van thanh")