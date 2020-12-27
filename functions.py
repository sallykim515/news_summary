import requests
from bs4 import BeautifulSoup
from gensim.summarization import summarize


def get_soup(url):
    r = requests.get(url)

    html_doc = r.text
    soup = BeautifulSoup(html_doc, 'lxml')

    return soup


def get_article(url):
    """
    :param url: full web address of the article
    :return: two objects - string title, string article content
    """
    soup = get_soup(url)
    article_tag = soup.find('article')

    title = article_tag.find('h1', {'id': 'main-heading'}).get_text()
    txt_blocks = article_tag.find_all('div', {'data-component': 'text-block'})

    article_content = ''
    for blk in txt_blocks:
        article_content += blk.get_text().strip() + '\n\n'

    return title, article_content


def summarize_article(url, ratio):
    """
    :param url: full web address of the article
    :param ratio: percentage
    :return:
    """
    title, content = get_article(url)

    # keep increasing the ratio until article summary returns
    summarized_text = ''
    while summarized_text == '':
        ratio += 0.01
        summarized_text = summarize(content, ratio=ratio)

    print('Title: ' + title)
    print('Summary: ' + '\n' + summarized_text + '\n')


def most_read_links(url):
    soup = get_soup(url)
    most_read_tag = soup.find('div', {'class': 'nw-c-most-read__items gel-layout gel-layout--no-flex'})

    links = []
    for link in most_read_tag.find_all('a'):
        links.append(link.get('href'))

    return links
