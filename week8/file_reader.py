with open ("py_digit.txt.py") as  file_object:
    contents = file_object.read()
    for line in file_object:
        print(line)