import requests
import os
from fake_useragent import UserAgent
import time

def generate_headers():
    ua = UserAgent()
    return {'user-agent':ua.random}

def get_comics_uni(path, url):
    try:
        i = 1
        p = requests.get(f'{url}/0{i}.jpg', headers=generate_headers())
        if p.status_code == 200:
            try:
                os.mkdir(path)
            except:
                pass
            out = open(f"{path}/00{i}.jpg", "wb")
            out.write(p.content)
            out.close()
            i += 1
            while p.status_code == 200:
                if i < 10:
                    p = requests.get(f'{url}/0{i}.jpg')
                    if p.status_code == 404:
                        break
                    out = open(f"{path}/00{i}.jpg", "wb")
                    out.write(p.content)
                    out.close()
                elif i < 100:
                    p = requests.get(f'{url}/{i}.jpg')
                    if p.status_code == 404:
                        break
                    out = open(f"{path}/0{i}.jpg", "wb")
                    out.write(p.content)
                    out.close()
                else:
                    p = requests.get(f'{url}/{i}.jpg')
                    if p.status_code == 404:
                        break
                    out = open(f"{path}/{i}.jpg", "wb")
                    out.write(p.content)
                    out.close()
                i += 1
    except:
        print('Отработка EXCEPT')
        time.sleep(10)
        get_comics_uni(path, url)
    

for x in range(252, 500):
    print(x)
    if x < 10:
        get_comics_uni(path=f'1 - RU\Человек-паук\Amazing\\Amazing Spider-Man #{x}', url=f'https://img1.unicomics.com/comics/amazing-spider-man/amazing-spider-man-00{x}')
    elif x < 100:
        get_comics_uni(path=f'1 - RU\Человек-паук\Amazing\\Amazing Spider-Man #{x}', url=f'https://img1.unicomics.com/comics/amazing-spider-man/amazing-spider-man-0{x}')
    else:
        get_comics_uni(path=f'1 - RU\Человек-паук\Amazing\\Amazing Spider-Man #{x}', url=f'https://img1.unicomics.com/comics/amazing-spider-man/amazing-spider-man-{x}')