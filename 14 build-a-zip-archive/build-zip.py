import zipfile
import os


def buildZip(path, file):
    with zipfile.ZipFile(file, "w") as z:
        os.chdir(path)
        for i in os.listdir(path):
            z.write(i)


buildZip("C:\\Users\\ademk\\OneDrive\\Masaüstü\\to_zip", "my_zip_file.zip")
