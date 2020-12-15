import requests
from bs4 import BeautifulSoup
from gensim.summarization import summarize


def get_soup(url):
    r = requests.get(url)

    html_doc = r.text
    soup = BeautifulSoup(html_doc, 'lxml')

    return soup


def get_article(url):

    soup = get_soup(url)
    article_tag = soup.find('article')

    title = article_tag.find('h1', {'id': 'main-heading'}).get_text()
    txt_blocks = article_tag.find_all('div', {'data-component': 'text-block'})

    article = title + '\n\n'
    for blk in txt_blocks:
        article += blk.get_text().strip() + '\n\n'

    return article


def summarize_article(url, ratio):
    article = get_article(url)

    idx = article.find('\n\n')

    print('Title: ' + article[: idx])
    print('Summary: ' + '\n' + summarize(article, ratio=ratio) + '\n')


def most_read_links(url):
    soup = get_soup(url)
    most_read_tag = soup.find('div', {'class': 'nw-c-most-read__items gel-layout gel-layout--no-flex'})

    links = []
    for link in most_read_tag.find_all('a'):
        links.append(link.get('href'))

    return links
