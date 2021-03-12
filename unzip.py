import zipfile
def unzip(path1, path2):
    fantasy_zip = zipfile.ZipFile(path1)
    fantasy_zip.extractall(path2)
    fantasy_zip.close()