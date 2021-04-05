import os
import img2pdf
import glob
import json
import PyPDF2
from multiprocessing import Process

#from parse import read_json


def colpage_pdf(path):
    pdf_file = open(path, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    num_pages = pdf_reader.numPages
    return num_pages


def read_json(path):
    with open(path, "r", encoding='utf-8') as read_file:
        data = json.load(read_file)
        return data


def img_to_pdf(path1, path2):
    for i in range(1, 1000):
        try:
            print(path2 + str(i))
            path = path1 + '/' + path2 + str(i)
            with open(f'{path}/{path2}{i}.pdf', "wb") as f:
                if len(glob.glob(path + "\*.jpg")) == 0:
                    print('---------' + str(i) + '-----------------')
                f.write(img2pdf.convert(glob.glob(path + "\*.jpg")))
        except:
            # print(i)
            pass


def get_path_json(json_data):
    sp_p = []
    for i in json_data['url_comics']['Marvel'].keys():
        for j in json_data['url_comics']['Marvel'][i].keys():
            path = [f"Comics/{i}/{j}", j + ' #']
            sp_p.append(path)
    return sp_p


# def img_to_pdf_mass()
#sp1 = get_path_json(read_json('data_json\comics.json'))
#for i in sp1:
#    img_to_pdf(i[0], i[1])
# img_to_pdf('1 - RU\Тор\Asgardians of the Galaxy', 'Asgardians of the Galaxy #')
# img_to_pdf('1 - RU\Тор\Beta Ray Bill - Godhunter', 'Beta Ray Bill - Godhunter #')
# img_to_pdf('1 - RU\Тор\Journey into Mystery', 'Journey into Mystery #')
# img_to_pdf('1 - RU\Тор\Journey into Mystery 2011', 'Journey into Mystery 2011 #')
# img_to_pdf('1 - RU\Тор\King Thor', 'King Thor #')
# img_to_pdf('1 - RU\Тор\Mighty Thor', 'Mighty Thor #')
# img_to_pdf('1 - RU\Тор\Mighty Thor - At the Gates of Valhalla', 'Mighty Thor - At the Gates of Valhalla #')
# img_to_pdf('1 - RU\Тор\Mighty Thor vol 2', 'Mighty Thor vol 2 #')
# img_to_pdf('1 - RU\Тор\Secret Invasion - Thor', 'Secret Invasion - Thor #')
# img_to_pdf('1 - RU\Тор\The Unworthy Thor', 'The Unworthy Thor #')
# img_to_pdf('1 - RU\Тор\Thor - Ages of Thunder', 'Thor - Ages of Thunder #')
# img_to_pdf('1 - RU\Тор\Thor - Blood Oath', 'Thor - Blood Oath #')
# img_to_pdf('1 - RU\Тор\Thor - for Asgard', 'Thor - for Asgard #')
# img_to_pdf('1 - RU\Тор\Thor - God of Thunder', 'Thor - God of Thunder #')
# img_to_pdf('1 - RU\Тор\Thor - Heaven and Earth', 'Thor - Heaven and Earth #')
# img_to_pdf('1 - RU\Тор\Thor - Son of Asgard', 'Thor - Son of Asgard #')
# img_to_pdf('1 - RU\Тор\Thor - The Deviants Saga', 'Thor - The Deviants Saga #')
# img_to_pdf('1 - RU\Тор\Thor - The Mighty Avenger', 'Thor - The Mighty Avenger #')
# img_to_pdf('1 - RU\Тор\Thor Vikings', 'Thor Vikings #')
# img_to_pdf('1 - RU\Тор\Thor vol 1', 'Thor vol 1 #')
# img_to_pdf('1 - RU\Тор\Thor vol 2', 'Thor vol 2 #')
# img_to_pdf('1 - RU\Тор\Thor vol 3', 'Thor vol 3 #')
# img_to_pdf('1 - RU\Тор\Thor vol 4', 'Thor vol 4 #')
# img_to_pdf('1 - RU\Тор\Thor vol 5', 'Thor vol 5 #')
# img_to_pdf('1 - RU\Тор\Thor vol 6', 'Thor vol 6 #')
# img_to_pdf('1 - RU\Локи\Loki - Agent of Asgard', 'Loki - Agent of Asgard #')
# img_to_pdf('1 - RU\Тор\Loki vol 1', 'Loki vol 1 #')
# img_to_pdf('1 - RU\Тор\Loki vol 2', 'Loki vol 2 #')
# img_to_pdf('1 - RU\Тор\Loki vol 3', 'Loki vol 3 #')
# img_to_pdf('1 - RU\Тор\Vote Loki', 'Vote Loki #')
# img_to_pdf('1 - RU\Человек-паук\Spidey', 'Spidey #')
# img_to_pdf('1 - RU\Человек-паук\Spectacular', 'Spectacular Spider-man #')
# img_to_pdf('1 - RU\Халк\Hulk', 'Hulk #')
# img_to_pdf('1 - RU\Мстители\Disassembled', 'Disassembled #')
# img_to_pdf('1 - RU\Мстители\Secret War', 'Secret War #')
# (colpage_pdf('1 - RU\Человек-паук\Amazing\Amazing Spider-Man #1\Amazing Spider-Man #1.pdf')
