import zipfile
with zipfile.ZipFile("D:\OIBGRIP-main.zip", 'r') as zip_ref:
    zip_ref.extractall("D:")