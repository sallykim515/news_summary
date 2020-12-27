import functions as fn

# ask users: single article, or Most read (10 articles)
bbc_url = 'https://www.bbc.com'
instruction = "Please type 'M' for Most Read articles, 'S' for a single article, 'X' to exit: "

resp = ''
while resp.upper() != 'X':
    resp = input(instruction)

    if resp.upper() == 'M':
        # most read option
        sub_links = fn.most_read_links(bbc_url + '/news')
        for i, lnk in enumerate(sub_links):
            print('Most Read #' + str(i+1))
            fn.summarize_article(bbc_url + lnk, 0.08)

    elif resp.upper() == 'S':
        # single article option
        url = input('Enter BBC News article link: ')
        fn.summarize_article(url, 0.08)

    elif resp.upper() != 'X':
        resp = input("Invalid input. " + instruction)

print('Thanks for using the news_summary. Bye now!')
