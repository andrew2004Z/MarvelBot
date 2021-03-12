import os
import img2pdf
import glob
def img_to_pdf(path1, path2):
    for i in range(59, 201):
        print(i)
        path = path1 + str(i)
        with open(f'{path}/{path2}{i}.pdf',"wb") as f:
            if len(glob.glob(path + "\*.jpg")) == 0:
                print('---------' + i + '-----------------')
            f.write(img2pdf.convert(glob.glob(path + "\*.jpg")))

img_to_pdf('1 - RU\Человек-паук\Amazing\Amazing Spider-Man #', 'Amazing Spider-Man #')