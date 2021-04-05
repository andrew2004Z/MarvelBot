import zipfile
def unzip(path1, path2):
    fantasy_zip = zipfile.ZipFile(path1)
    fantasy_zip.extractall(path2)
    fantasy_zip.close()

for i in range(100000000):
    if 6400 ** 2 + 2 * 6400 * i + i ** 2 == 16 * 6400:
        print(i)