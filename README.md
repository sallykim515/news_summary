# news_summary
A python program that summarizes an article (or all 10 articles under Most Read section) from BBC news (https://www.bbc.com/news) using `gensim` package. The default is set to 5% ratio.

# Example
For a single article summary, type 'S' and paste the article's link:
![news_summary_example](https://user-images.githubusercontent.com/39283556/102278837-51723380-3edf-11eb-990a-4ce62c59dae6.PNG)

For all 10 articles under Most Read section, type 'M':
![news_summary_example3](https://user-images.githubusercontent.com/39283556/102278840-53d48d80-3edf-11eb-9b22-4131cfd1744e.PNG)

To exit, type 'X':
![news_summary_example2](https://user-images.githubusercontent.com/39283556/102278845-5636e780-3edf-11eb-995e-268d377d4bee.PNG)

# Behind the Scene
Libraries used:
`requests`, `bs4`, `gensim`

# Potential Future Features:
* option to email the summary
* auto-adjust the ratio such that if the default ratio is too small to return any summary, re-summerize with an increased ratio
