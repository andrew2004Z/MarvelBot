import requests
import os
from fake_useragent import UserAgent
import time
import glob
import img2pdf
from image_to_pdf import img_to_pdf
from bs4 import BeautifulSoup
import json
import telebot

bot = telebot.TeleBot('1417817254:AAGRJdZkQSsNgWZO7Sfp8REFD1aepTPSGJg')

def generate_headers():
    ua = UserAgent()
    return {'user-agent': ua.random}


def get_comics_uni(path, url, col_null, g):
    try:
        i = g
        if col_null == 2:
            p = requests.get(f'{url}/00{i}.jpg', headers=generate_headers())
        else:
            p = requests.get(f'{url}/0{i}.jpg', headers=generate_headers())
        if p.status_code == 200:
            try:
                os.mkdir(path)
            except:
                pass
            if g == 0:
                out = open(f"{path}/00{i + 1}.jpg", "wb")
            else:
                out = open(f"{path}/00{i}.jpg", "wb")
            out.write(p.content)
            out.close()
            i += 1
            while p.status_code == 200:
                if i < 10:
                    if col_null == 2:
                        p = requests.get(f'{url}/00{i}.jpg',
                                         headers=generate_headers())
                    else:
                        p = requests.get(f'{url}/0{i}.jpg',
                                         headers=generate_headers())
                    if p.status_code == 404:
                        break
                    if g == 0 and i == 9:
                        out = open(f"{path}/0{i + 1}.jpg", "wb")
                    elif g == 0:
                        out = open(f"{path}/00{i + 1}.jpg", "wb")
                    else:
                        out = open(f"{path}/00{i}.jpg", "wb")
                    out.write(p.content)
                    out.close()
                elif i < 100:
                    if col_null == 2:
                        p = requests.get(f'{url}/0{i}.jpg',
                                         headers=generate_headers())
                    else:
                        p = requests.get(f'{url}/{i}.jpg',
                                         headers=generate_headers())
                    if p.status_code == 404:
                        break
                    if g == 0:
                        out = open(f"{path}/0{i + 1}.jpg", "wb")
                    else:
                        out = open(f"{path}/0{i}.jpg", "wb")
                    out.write(p.content)
                    out.close()
                else:
                    if col_null == 2:
                        p = requests.get(f'{url}/{i}.jpg',
                                         headers=generate_headers())
                    else:
                        p = requests.get(f'{url}/{i}.jpg',
                                         headers=generate_headers())
                    if p.status_code == 404:
                        break
                    if g == 0:
                        out = open(f"{path}/{i + 1}.jpg", "wb")
                    else:
                        out = open(f"{path}/{i}.jpg", "wb")
                    out.write(p.content)
                    out.close()
                i += 1
        # print(path.split('\\')[-1].split('#')[0] + '#')

    except ConnectionError:
        print('ConnectionError')
        time.sleep(10)
        get_comics_uni(path, url, col_null, g=g)
    except TimeoutError:
        time.sleep(10)
        get_comics_uni(path, url, col_null, g=g)
    #except Exception as e:
    #    bot.send_message('604900292', e)
    #    bot.send_message('604900292', path)
    #    return None

def run_get_comics_uni(path11, url, sp_num):
    for x in range(sp_num[0], sp_num[1]):
        #print(x)
        # path1 = f'1 - RU\Тор\Thor - for Asgard\\Thor - for Asgard #{x}'
        path1 = path11 + str(x)
        if x < 10:
            url1 = url + f'00{x}'
        elif x < 100:
            url1 = url + f'0{x}'
        else:
            url1 = url + f'{x}'
        if not os.path.exists(path1 + '/' + path1.split('/')[-1] + '.pdf'):
            print(path1 + '/' + path1.split('/')[-1] + '.pdf')
            #sp.append([path1, url1, 2, 0])
            get_comics_uni(path=path1, url=url1, col_null=2, g=0)
        else:
            print('File found: ' + path1)
        # print('\\'.join(path11.split('\\')[0:-1]))
        # print(path11.split('\\')[-1])
    #img_to_pdf('\\'.join(path11.split('\\')[0:-1]), path11.split('\\')[-1])


def run_get_comics_one(path11, url, sp_num):
    for x in range(sp_num[0], sp_num[1]):
        #print(x)
        # path1 = f'1 - RU\Тор\Thor - for Asgard\\Thor - for Asgard #{x}'
        path1 = path11 + str(x)
        if x < 10:
            url1 = url + f'00{x}'
        elif x < 100:
            url1 = url + f'0{x}'
        else:
            url1 = url + f'{x}'
        get_comics_uni(path=path1, url=url1, col_null=2, g=0)
        # print('\\'.join(path11.split('\\')[0:-1]))
        # print(path11.split('\\')[-1])
    #img_to_pdf('\\'.join(path11.split('\\')[0:-1]), path11.split('\\')[-1])


def get_name_comics(url):
    sp1 = []
    sp = []
    sp2 = []
    sp3 = []
    p = requests.get(url, headers=generate_headers()).content
    soup = BeautifulSoup(p, 'lxml')
    ui = soup.find_all('h4', class_='field-content')
    for i in ui:
        sp.append([i.text, 'https://drawnstories.ru/' + i.find('a')['href']])
    for i in sp:
        p1 = requests.get(i[1], headers=generate_headers()).content
        soup1 = BeautifulSoup(p1, 'lxml')
        ui1 = soup1.find_all('h4', class_='field-content')
        for i in ui1:
            sp1.append(
                [i.text, 'https://drawnstories.ru/' + i.find('a')['href']])
    for i in sp1:
        p2 = requests.get(i[1], headers=generate_headers()).content
        soup2 = BeautifulSoup(p2, 'lxml')
        soup3 = BeautifulSoup(p2, 'lxml')
        h1 = soup2.find('h1', class_='page-header').text
        try:
            sp_v = soup3.find_all(
                'div', class_='field-item even')[1].find_all('div')
        except IndexError as e:
            pass
        for i in sp_v:
            try:
                url11 = i.find('a')['href']
                if 'http' in url11 and 'vk.com' not in url11:
                    sp_path = url11[:-11][:-1].split('/')[-1].split('-')
                    path = []
                    for i in sp_path:
                        path.append(i.capitalize())
                    # print(f"1 - RU/{' '.join(path)}/{' '.join(path)} #".split('/')[:-1])
                    if url11[:-11][-1] == '-':
                        sp3.append(['1 - RU/' + ' '.join(path) +
                                    ' '.join(path) + ' #', url11[:-11]])
                        break
            except Exception as e:
                pass
    for i in sp3:
        try:
            os.mkdir(i[0].split('/')[-2])
        except:
            pass
        run_get_comics_uni(i[0], i[1], [1, 1000])
        #sp2.append([h1, soup2.find('div', class_='nav1').find('a')['href']])
    # print(sp2)


def parse_add_json(url):
    p = requests.get(url)
    if p.status_code == 200:
        soup = BeautifulSoup(p.content, 'lxml')
        dict1 = {}
        dict1[soup.find('h1', class_='page-header').text] = {}
        for i in soup.find_all('div', 'views-field views-field-name'):
            #dict1[soup.find('h1', class_='page-header').text][i.find('a').text] = ''
            try:
                p1 = requests.get(
                    'https://drawnstories.ru/' + i.find('a')['href'])
                if p.status_code == 200:
                    soup1 = BeautifulSoup(p1.content, 'lxml')
                    # print(soup1.find('h1'))
                    try:
                        dict1[soup.find('h1', class_='page-header').text][soup1.find('h1').text.split(' / ')[-1]] = soup1.find('div', class_='big1').find('img')['src'][:-5]
                    except:
                        dict1[soup.find('h1', class_='page-header').text][soup1.find('h1').text.split(' / ')[-1]] = soup1.find('div', class_='ds11').find('img')['src'][:-5]
                else:
                    print('ERORR')
            except Exception as e:
                print(e)
        with open("data_file.json", "a", encoding='utf-8') as write_file:
            json.dump(dict1, write_file, ensure_ascii=False)
    else:
        print('ERORR 404')
#parse_add_json('https://drawnstories.ru/comics/Marvel-Comics/black-widow')
#parse_add_json('https://drawnstories.ru/comics/Marvel-Comics/black-panther')
#parse_add_json('https://drawnstories.ru/comics/marvel-comics/what-if')
#parse_add_json('https://drawnstories.ru/comics/marvel-comics/foolkiler')
#parse_add_json('https://drawnstories.ru/comics/Marvel-Comics/SHIELD')
#parse_add_json('https://drawnstories.ru/comics/marvel-comics/Elektra')
#parse_add_json('https://drawnstories.ru/comics/marvel-comics/union-jack')
#parse_add_json('https://drawnstories.ru/comics/Marvel-Comics/Fantastic-Four')
#parse_add_json('https://drawnstories.ru/comics/marvel-comics/hulk')
#parse_add_json('https://drawnstories.ru/comics/marvel-comics/Halo')
#parse_add_json('https://drawnstories.ru/comics/marvel-comics/Hawkeye')
#parse_add_json('https://drawnstories.ru/comics/marvel-comics/ant-man')
#parse_add_json('https://drawnstories.ru/comics/marvel-comics/Spider-Man')


def read_json(path):
    with open(path, "r", encoding='utf-8') as read_file:
        data = json.load(read_file)
        return data

def parse_json(json_parse):
    for i in json_parse['url_comics']['Marvel'].keys():
        try:
            os.mkdir('Comics/' + i)
        except:
            pass
        for j in json_parse['url_comics']['Marvel'][i].keys():
            try:
                os.mkdir('Comics/' + i + '/' + j.replace(':', " -"))
            except:
                pass
            run_get_comics_uni('Comics/' + i + '/' + j.replace(':', " -") + '/' + j.replace(':', " -") + ' #', json_parse['url_comics']['Marvel'][i][j], [0, 200])


parse_json(read_json('data_json\comics1.json'))

# run_get_comics_uni('1 - RU\Тор\Thor - Blood Oath\\Thor - Blood Oath #', 'https://img.drawnstories.ru/img/Marvel-Comics/thor/Thor-Blood-Oath/Thor-Blood-Oath-', [1, 105])
# run_get_comics_uni('1 - RU\Тор\King Thor\\King Thor #', 'https://img.drawnstories.ru/img/Marvel-Comics/thor/king-thor/king-thor-', [1, 105])
# run_get_comics_uni('1 - RU\Локи\Loki - Agent of Asgard\\Loki - Agent of Asgard #', 'https://img.drawnstories.ru/img/Marvel-Comics/thor/loki/agent-of-asgard/agent-of-asgard-', [1, 125])
# run_get_comics_uni('1 - RU\Локи\Vote Loki\\Vote Loki #', 'https://img.drawnstories.ru/img/Marvel-Comics/thor/loki/vote-loki/vote-loki-', [1, 105])
# run_get_comics_uni('1 - RU\Локи\Loki vol 1\\Loki vol 1 #', 'https://img.drawnstories.ru/img/Marvel-Comics/thor/loki/loki-v1/loki-v1-', [1, 105])
# run_get_comics_uni('1 - RU\Локи\Loki vol 2\\Loki vol 2 #', 'https://img.drawnstories.ru/img/Marvel-Comics/thor/loki/loki-v2/loki-v2-', [1, 105])
# run_get_comics_uni('1 - RU\Локи\Loki vol 3\\Loki vol 3 #', 'https://img.drawnstories.ru/img/Marvel-Comics/thor/loki/loki-v3/loki-v3-', [1, 105])

# run_get_comics_uni('1 - RU\Тор\Thor - The Mighty Avenger\Thor - The Mighty Avenger #', 'https://img.drawnstories.ru/img/Marvel-Comics/thor/the-mighty-avenger/the-mighty-avenger-', [1, 105])
# run_get_comics_uni('1 - RU\Тор\Mighty Thor\Mighty Thor #', 'http://img.drawnstories.ru/img/Marvel-Comics/thor/mighty-thor/mighty-thor-', [1, 105])
# run_get_comics_uni('1 - RU\Тор\Mighty Thor vol 2\Mighty Thor vol 2 #', 'http://img.drawnstories.ru/img/Marvel-Comics/thor/The-Mighty-Thor-v2/The-Mighty-Thor-v2-', [1, 105])
# run_get_comics_uni('1 - RU\Тор\Thor - Heaven and Earth\Thor - Heaven and Earth #', 'http://img.drawnstories.ru/img/Marvel-Comics/thor/Thor-Heaven-Earth/Thor-Heaven-Earth-', [1, 105])
# run_get_comics_uni('1 - RU\Тор\The Unworthy Thor\The Unworthy Thor #', 'http://img.drawnstories.ru/img/Marvel-Comics/thor/The-Unworthy-Thor/The-Unworthy-Thor-', [1, 105])
# run_get_comics_uni('1 - RU\Тор\Journey into Mystery\Journey into Mysteryr #', 'http://img.drawnstories.ru/img/Marvel-Comics/thor/journey-into-mystery/journey-into-mystery-', [1, 140])
# run_get_comics_uni('1 - RU\Тор\Journey into Mystery 2011\Journey into Mystery 2011 #', 'http://img.drawnstories.ru/img/Marvel-Comics/thor/journey-into-mystery-2011/journey-into-mystery-2011-', [1, 1000])
# run_get_comics_uni('1 - RU\Тор\Secret Invasion - Thor\Secret Invasion - Thor #', 'http://img.drawnstories.ru/img/Marvel-Comics/thor/secret-invasion/secret-invasion-', [1, 105])
# run_get_comics_uni('1 - RU\Тор\Ultimate Comics Thor\Ultimate Comics Thor #', 'http://img.drawnstories.ru/img/Marvel-Comics/thor/ultimate-thor/ultimate-thor-', [1, 105])
# run_get_comics_uni('1 - RU\Тор\Thor - Son of Asgard\Thor - Son of Asgard #', 'http://img.drawnstories.ru/img/Marvel-Comics/thor/Thor-Son-of-Asgard/Thor-Son-of-Asgard-', [1, 105])
# run_get_comics_uni('1 - RU\Тор\Thor - The Deviants Saga\Thor - The Deviants Saga #', 'http://img.drawnstories.ru/img/Marvel-Comics/thor/thor-deviants-saga/thor-deviants-saga-', [1, 105])
# run_get_comics_uni('1 - RU\Тор\Mighty Thor - At the Gates of Valhalla\Mighty Thor - At the Gates of Valhalla #', 'http://img.drawnstories.ru/img/Marvel-Comics/thor/the-mighty-thor-at-the-gates-of-valhalla/the-mighty-thor-at-the-gates-of-valhalla-', [1, 105])
#
#
# run_get_comics_uni('1 - RU\Тор\Thor vol 1\Thor vol 1 #', 'http://img.drawnstories.ru/img/Marvel-Comics/thor/thor-v1/thor-v1-', [1, 1000])
# run_get_comics_uni('1 - RU\Тор\Thor vol 2\Thor vol 2 #', 'http://img.drawnstories.ru/img/Marvel-Comics/thor/thor-v1/thor-v2-', [1, 1000])
# run_get_comics_uni('1 - RU\Тор\Thor vol 3\Thor vol 3 #', 'http://img.drawnstories.ru/img/Marvel-Comics/thor/thor-v1/thor-v3-', [1, 1000])
# run_get_comics_uni('1 - RU\Тор\Thor vol 4\Thor vol 4 #', 'http://img.drawnstories.ru/img/Marvel-Comics/thor/thor-v1/thor-v4-', [1, 1000])
# run_get_comics_uni('1 - RU\Тор\Thor vol 5\Thor vol 5 #', 'http://img.drawnstories.ru/img/Marvel-Comics/thor/thor-v1/thor-v5-', [1, 1000])
# run_get_comics_uni('1 - RU\Тор\Thor vol 6\Thor vol 6 #', 'http://img.drawnstories.ru/img/Marvel-Comics/thor/thor-v1/thor-v6-', [1, 1000])
# run_get_comics_uni('1 - RU\Тор\Thor vol 6\Thor vol 6 #', 'http://img.drawnstories.ru/img/Marvel-Comics/thor/thor-v1/thor-v6-', [1, 1000])
#
# run_get_comics_uni('1 - RU\Тор\Thor - Ages of Thunder\Thor - Ages of Thunder #', 'http://img.drawnstories.ru/img/marvel-comics/thor/ages-of-thunder/ages-of-thunder-', [1, 105])

# run_get_comics_uni('1 - RU\Человек-паук\Marvel Action - Spider-Man\\Marvel Action - Spider-Man #', 'http://img.drawnstories.ru/img/Marvel-comics/Spider-Man/marvel-action-spider-man/marvel-action-spider-man-', [1, 5])
# run_get_comics_uni('1 - RU\Человек-паук\Scarlet Spider vol 1\Scarlet Spider vol 1 #', 'http://img.drawnstories.ru/img/Marvel-Comics/Spider-Man/Scarlet-Spider/Scarlet-Spider-v1/Scarlet-Spider-v1-', [1, 105])
# run_get_comics_uni('1 - RU\Человек-паук\Ben Reilly - The Scarlet Spider\Ben Reilly - The Scarlet Spider #', 'http://img.drawnstories.ru/img/Marvel-Comics/Spider-Man/Scarlet-Spider/Ben-Reilly/Ben-Reilly-', [1, 105])
# run_get_comics_uni('1 - RU\Человек-паук\Prowler\Prowler #', 'http://img.drawnstories.ru/img/Marvel-Comics/Spider-Man/Prowler/Prowler-', [1, 5])
# run_get_comics_uni('1 - RU\Человек-паук\Web Warriors\Web Warriors #', 'http://img.drawnstories.ru/img/Marvel-Comics/Spider-Man/Web-Warriors/Web-Warriors-', [1, 105])
# run_get_comics_uni('1 - RU\Человек-паук\Spider-Man - Newspaper Strips\Spider-Man - Newspaper Strips #', 'http://img.drawnstories.ru/img/Marvel-Comics/Spider-Man/newspaper-strips/newspaper-strips-', [1, 105])
# run_get_comics_uni('1 - RU\Человек-паук\Spider-Gwen\Spider-Gwen #', 'http://img.drawnstories.ru/img/Marvel-Comics/Spider-Man/Spider-Gwen/Spider-Gwen-', [1, 105])
# run_get_comics_uni('1 - RU\Человек-паук\Spider-Gwen vol 2\Spider-Gwen vol 2 #', 'http://img.drawnstories.ru/img/Marvel-Comics/Spider-Man/Spider-Gwen-v2/Spider-Gwen-v2-', [1, 105])
# get_name_comics('https://drawnstories.ru/comics/marvel-comics')
