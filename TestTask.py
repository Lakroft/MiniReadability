# -*- coding: utf-8 -*-
import sys
import validators
import requests
from bs4 import BeautifulSoup
import os


def format(text):
    #print(("format"))
    text = text.replace('\n', '')  # удалять переносы
    strlen = len(text)
    strstart = 0
    prev = 0
    last = 0
    while last < strlen:  # ставить переносы, делая строки по 80 символов
        last = text.find(' ', last)
        if last < 0:
            break
        if ((last - strstart > 80)):
            text = text[:prev] + '\n' + text[prev + 1:]
            strstart = prev + 1
        prev = last
        last += 1
    return text


def parse(text):
    soup = BeautifulSoup(text, "html.parser")
    for link in soup.select('a'):  # Заменяем ссылки на текст и адрес в скобках
        text = link.getText()
        try:
            text += ' [' + link['href'] + ']'
        except KeyError:
            continue
        link.replaceWith(text)
    res = ''
    for text in soup.find_all('h1'):  # Добавляем заголовок
        res += text.getText()
    res += '\n\n'
    for text in soup.find_all('p'):  # Добавляем текст статьи
        res += format(text.getText())
        res += '\n\n'
    return res


def saveFile(url, text):
    homedir = os.getcwd()
    partsOfURL = url.split('/')
    partlength = len(partsOfURL) - 1
    addr = ''
    filename = ''
    if partsOfURL[partlength] == '':
        partlength -= 1
    for part in partsOfURL[2:]:
        if part != partsOfURL[partlength]:
            addr += '\\' + part
        else:
            filename = part.split('.')[0] + '.txt'
            break
    try:
        os.makedirs(homedir + addr)
    except WindowsError:
        pass
    os.chdir(homedir + addr)
    print(("save: " + addr + filename + '\n'))
    with open(filename, 'w') as outFile:
        outFile.write(text)  # сохраняем в файл
    os.chdir(homedir)

for param in sys.argv[1:]:
    if not ((validators.url(param))):  # проверяем, что это валидный урл
        print ((param + ' is not valid url'))
    else:
        print(("get"))
        r = requests.get(param)  # получаем страницу
        print(("parse"))
        result = parse(r.text)  # преобразуем
        saveFile(param, result.encode('utf-8'))