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

    
    num = 1


    stuff_for_frontend = {
        'final_postings': final_posting,
        'num' : num
    }

    return render(request , 'home.html' ,stuff_for_frontend )



def article(request):
    link = request.POST.get('article_')
    p,q,r,s = news.full_news(link)
    print(link)
    final_posting = []
    final_posting.append([p,q,r,s])
    num = 1
    stuff_for_frontend = {
        'final_postings': final_posting,
        'num' : num
    }
    return render(request, 'news.html' ,stuff_for_frontend)


def sports(request):
    titles_S , links_S , dates_S , descriptions_S , images_S = news.news_articles('https://indianexpress.com/section/sports/')
    final_posting = []
    for i in range(len(titles_S)):
        final_posting.append((titles_S[i] , links_S[i] , dates_S[i] , descriptions_S[i] , images_S[i]))

    
    
    num = 1

    stuff_for_frontend = {
        'final_postings': final_posting,
        'num' : num
    }

    return render(request , 'sports.html' ,stuff_for_frontend )


def entertainment(request):
    #titles , links , dates , descriptions , images = news.news_articles(valid_urls[3])
    final_posting = []
    #for i in range(len(titles)):
    #    final_posting.append((titles[i] , links[i] , dates[i] , descriptions[i] , images[i]))
#
    
    


    stuff_for_frontend = {
        'final_postings': final_posting
    }

    return render(request , 'entertainment.html' ,stuff_for_frontend )

def lifestyle(request):
    titles , links , dates , descriptions , images = news.news_articles(valid_urls[4])
    final_posting = []
    for i in range(len(titles)):
        final_posting.append((titles[i] , links[i] , dates[i] , descriptions[i] , images[i]))

    
    
    num = 1

    stuff_for_frontend = {
        'final_postings': final_posting,
        'num' : num
    }

    return render(request , 'lifestyle.html' ,stuff_for_frontend )


def cities(request):
    titles , links , dates , descriptions , images = news.news_articles(valid_urls[2])
    final_posting = []
    for i in range(len(titles)):
        final_posting.append((titles[i] , links[i] , dates[i] , descriptions[i] , images[i]))

    
    
    num = 1

    stuff_for_frontend = {
        'final_postings': final_posting,
        'num' : num
    }

    return render(request , 'cities.html' ,stuff_for_frontend )


def pages(request , val   , num ):
    if val == 'home':
        
        titles , links , dates , descriptions , images = news.news_articles(f'https://indianexpress.com/section/india/page/{num}/')
        final_posting = []
        for i in range(len(titles)):
            final_posting.append((titles[i] , links[i] , dates[i] , descriptions[i] , images[i]))
        stuff_for_frontend = {
            'final_postings': final_posting,
            'num' : num
        }

        return render(request , 'home.html' ,stuff_for_frontend )
    elif val == 'sports':
        
        titles , links , dates , descriptions , images = news.news_articles(f'https://indianexpress.com/section/{val}/page/{num}/')
        final_posting = []
        for i in range(len(titles)):
            final_posting.append((titles[i] , links[i] , dates[i] , descriptions[i] , images[i]))
       


        stuff_for_frontend = {
            'final_postings': final_posting,
            'num' : num
        }

        return render(request , 'sports.html' ,stuff_for_frontend )
    
    elif val == 'lifestyle':
        
        titles , links , dates , descriptions , images = news.news_articles(f'https://indianexpress.com/section/{val}/page/{num}/')
        final_posting = []
        for i in range(len(titles)):
            final_posting.append((titles[i] , links[i] , dates[i] , descriptions[i] , images[i]))
       


        stuff_for_frontend = {
            'final_postings': final_posting,
            'num' : num
        }

        return render(request , 'lifestyle.html' ,stuff_for_frontend )
    
    elif val == 'cities':
        
        titles , links , dates , descriptions , images = news.news_articles(f'https://indianexpress.com/section/{val}/page/{num}/')
        final_posting = []
        for i in range(len(titles)):
            final_posting.append((titles[i] , links[i] , dates[i] , descriptions[i] , images[i]))
       


        stuff_for_frontend = {
            'final_postings': final_posting,
            'num' : num
        }

        return render(request , 'cities.html' ,stuff_for_frontend )
    