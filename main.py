import functions as fn

url = input("Enter BBC News article link: ")

article = fn.get_article(url)
fn.summarize_article(article, 0.05)

