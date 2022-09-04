# Web Scraping

→ 웹 상의 데이터를 추출하는 것

제작환경

(https://repl.it/)

접속대상

- (https://www.indeed.com/q-python-jobs.html)
- (https://www.indeed.com/jobs?as_and=python&limit=50)
- (https://stackoverflow.com/jobs?q=python)

python으로 URL에서 자료 추출하기

- python 기본 라이브러리 urllib : 사용x, 더 강력한 온라인 라이브러리 사용하기 위해
- Request 사용o

(https://requests.readthedocs.io/projects/3/)

(https://github.com/psf/requests)

HTML에서 정보추출하기

- Beautiful Soup4

(https://www.crummy.com/software/BeautifulSoup/)

## requests

→ 데이터 크롤링을 위한 패키지를 소개

→ url을 베이스로 html데이터를 크롤링할 수 있는데 html데이터만을 가지고 필요로 하는 데이터(직업 데이터, 총 데이터 수량 등등)를 뽑아내는 것은 비효율적

## Beautiful Soup

[Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/)

[뷰티플수프 문서 - 뷰티플수프 4.0.0 문서](https://www.crummy.com/software/BeautifulSoup/bs4/doc.ko/)

```python
#Example:

pagination = soup.find("div", class_="s-pagination")
pagination = soup.find("div", "class": "s-pagination")
```

```python
#Example:

soup("div", class_="-job")
soup.find_all("div", "class": "-job")
```