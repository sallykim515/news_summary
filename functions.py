import requests
from bs4 import BeautifulSoup
from gensim.summarization import summarize


def get_article(url):
    r = requests.get(url)

    html_doc = r.text
    soup = BeautifulSoup(html_doc, 'lxml')

    article_tag = soup.find('article')

    title = article_tag.find('h1', {'id': 'main-heading'}).get_text()
    txt_blocks = article_tag.find_all('div', {'data-component': 'text-block'})

    article = title + '\n\n'
    for blk in txt_blocks:
        article += blk.get_text().strip() + '\n\n'

    return article

def summarize_article(article, ratio):
    idx = article.find('\n\n')

    print()
    print("Title: " + article[: idx])
    print()
    print("Summary: " + "\n" + summarize(article, ratio=ratio))
