from bs4 import BeautifulSoup as bs
import requests
header = {'useragent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"}
url = 'https://thehackernews.com/'
def article(url):
    
    page = requests.get(url)
    soup = bs(page.content,'html.parser')
        #print(soup)
    all_titles= []
    all_images = []
    all_descriptions = []
    all_urls = []
    all_dates = []
    articles = soup.find_all(class_="clear home-post-box cf")
    #print(articles)
    for article in articles:

        all_titles.append(article.find(class_ = 'home-title').get_text())
        all_images.append(article.find(class_ ="home-img clear").find(class_ = 'img-ratio').img['data-src'])
        #all_urls.append(article.find(class_ ="body-post clear").a['href'])
        all_dates.append(article.find(class_ ="item-label").get_text())
        all_descriptions.append(article.find(class_ = 'home-desc').get_text())

    #print(all_urls)
    #print(all_images)
    #print(all_dates)
    #print(all_descriptions)
    return all_titles, all_dates , all_descriptions , all_images
#print(article(url))
