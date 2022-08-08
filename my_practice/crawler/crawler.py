import requests

def crawl(url):
    data = requests.get(url)
    print(data, url)
    return data.content

url = "https://cafe.naver.com/re4mo?iframe_url=/ArticleList.nhn%3Fsearch.clubid=13988016%26search.menuid=330%26search.boardtype=L"

pageString = crawl(url)
print(pageString)