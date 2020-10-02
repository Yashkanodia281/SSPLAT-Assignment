
from django.shortcuts import render
from newsapi import NewsApiClient


def Index(request):
    newsapi = NewsApiClient(api_key="a195aa9bd9c147bbbba3f003108f7df5")
    topheadlines = newsapi.get_top_headlines(sources='al-jazeera-english')

    articles = topheadlines['articles']

    desc = []
    news = []
    img = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])

    mylist = zip(news, desc, img)

    return render(request, 'index.html', context={"mylist": mylist})


def bbc(request):
    newsapi = NewsApiClient(api_key="a195aa9bd9c147bbbba3f003108f7df5")
    #topheadlines = newsapi.get_top_headlines(sources='bbc-news')
    topheadlines = newsapi.get_everything(sources='bbc-news')
    articles = topheadlines['articles']
    aut=[]
    desc = []
    news = []
    img = []
    publishAt=[]


    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        aut.append(myarticles['author'])
        publishAt.append(myarticles['publishedAt'])



    mylist = zip(news, desc, img, publishAt, aut)

    return render(request, 'bbc.html', context={"mylist": mylist})
