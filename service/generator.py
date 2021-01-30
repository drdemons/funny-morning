from bs4 import BeautifulSoup
import requests
import random


def __pagination():
    anekdoty = requests.get('https://anekdoty.ru/pro-programmistov/')
    soup = BeautifulSoup(anekdoty.text, 'lxml')
    pages = soup.find('ul', class_='pagination')
    links = pages.find_all('a')
    urls = [link.get('href') for link in links]
    urls.append(anekdoty.url)
    return urls


def __anecdotes(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')
    find_all_anecdotes = soup.find_all('div', class_='text-holder')
    return [paragraph.find('p').getText() for paragraph in find_all_anecdotes]


def generate():
    urls = __pagination()
    url = random.choice(urls)
    return random.choice(__anecdotes(url))
