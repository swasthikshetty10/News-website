from django.shortcuts import render
from . import theindianexpress as news
# Create your views here.
valid_urls = ['https://indianexpress.com/section/india/',
              'https://indianexpress.com/section/sports/',
              'https://indianexpress.com/section/cities/',
              'https://indianexpress.com/section/entertainment/',
              'https://indianexpress.com/section/lifestyle/',

              ]
def home(request):
    titles , links , dates , descriptions , images = news.news_articles(valid_urls[0])
    final_posting = []
    for i in range(len(titles)):
        final_posting.append((titles[i] , links[i] , dates[i] , descriptions[i] , images[i]))

    
    


    stuff_for_frontend = {
        'final_postings': final_posting
    }

    return render(request , 'home.html' ,stuff_for_frontend )



def article(request):
    link = request.POST.get('article_')
    p,q,r,s = news.full_news(link)
    print(link)
    final_posting = []
    final_posting.append([p,q,r,s])
    stuff_for_frontend = {
        'final_postings': final_posting
    }
    return render(request, 'news.html' ,stuff_for_frontend)