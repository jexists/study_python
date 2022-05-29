## namespacing

 template > view > index.html

view.py

```jsx
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request): #첫번째 파라미터: request
  return render(request, 'posts/index.html')
  # print('로그 남기기: 디버깅')
  # return HttpResponse('Hello World!')
  # http://localhost:8000/posts/ -> 실행

def detail(request, post_id):
  return HttpResponse(f'post: {post_id}!')

def comment(request, post_id):
  return HttpResponse('Hello comment!')
```

settings.py

→ 장고 App만들면  installed_apps 추가

→ posts.apps.PostsConfig 또는 posts로 입력

```jsx
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'posts',
#posts대신 posts.apps.PostsConfig 로 등록가능
]
```

## context

→ 딕셔너리, 리스트, 클래스 등 사용

```jsx
<!DOCTYPE html>
<html lang="ko">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Jestagram</title>
</head>

<body>
  <h1>posts</h1>

  <ul>
    <li>{{post}}</li>
  </ul>

</body>

</html>
```

```jsx
def index(request): #첫번째 파라미터: request
  return render(request, 'posts/index.html', {context 작성 가능})
```

```jsx
def index(request): #첫번째 파라미터: request
  context = {
    'key': 'value'
  }
  return render(request, 'posts/index.html', context)
```

```jsx
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request): #첫번째 파라미터: request
  context = {
    'post': 'html {{post}} 대신나옴'
  }
  return render(request, 'posts/index.html', context)

  # return render(request, 'posts/index.html', {context 작성 가능})
  # print('로그 남기기: 디버깅')
  # return HttpResponse('Hello World!')
  # http://localhost:8000/posts/ -> 실행

def detail(request, post_id):
  return HttpResponse(f'post: {post_id}!')

def comment(request, post_id):
  return HttpResponse('Hello comment!')
```

---

```jsx
#view.py
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
class Member:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
def index(request): #첫번째 파라미터: request
  context = {
    'post': {
      'author': 'jexists',
      'summary': 'django project'},
      #dictionary
      'numbers': [10,20, 30],
      #list
      'member': Member('jexists', 20)
      #class instance
  }
  return render(request, 'posts/index.html', context)
  # return render(request, 'posts/index.html', {context 작성 가능})
  # print('로그 남기기: 디버깅')
  # return HttpResponse('Hello World!')
  # http://localhost:8000/posts/ -> 실행

def detail(request, post_id):
  return HttpResponse(f'post: {post_id}!')

def comment(request, post_id):
  return HttpResponse('Hello comment!')
```

```jsx
#index.html
<!DOCTYPE html>
<html lang="ko">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Jestagram</title>
</head>

<body>
  <h1>posts</h1>

  <h2>dictionary</h2>
  <ul>
    <li>Author: {{post.author}}</li>
    <li>Summary: {{post.summary}}</li>
  </ul>

  <h2>list number</h2>
  <ul>
    <li>{{numbers.0}}</li>
    <li>{{numbers.1}}</li>
    <li>{{numbers.2}}</li>
  </ul>
  
  <h2>class</h2>
  <ul>
    <li>Name: {{member.name}}</li>
    <li>Age: {{member.age}}</li>
  </ul>

</body>

</html>
```

## for 문

→{% for post in posts %} 반복내용 {% endfor %}

→ 

```jsx
context = {
    'posts': [
      {'author': 'joy', 'summary': 'book1'},
      {'author': 'sadness', 'summary': 'book2'},
      {'author': 'anger', 'summary': 'book3'}
    ]
    
  }
  return render(request, 'posts/index.html', context)
```

```jsx
<h1>posts</h1>

  <ul>
    <li>Author: {{ posts.0.author }} || Summary: {{ posts.0.summary }}</li>
    <li>Author: {{ posts.1.author }} || Summary: {{ posts.1.summary }}</li>
    <li>Author: {{ posts.2.author }} || Summary: {{ posts.2.summary }}</li>
  </ul>
```

```jsx
<h1>posts</h1>

  <ul>
    {% for post in posts %}
      <li>Author: {{ post.author }} || Summary: {{ post.summary }}</li>
    {% endfor %}
  </ul>
```

## if 문

→ {% if post %}내용 {%else%}내용 {% endif %}

```jsx
{% if posts %}
  <ul>
    {% for post in posts %}
      <li>Author: {{ post.author }} || Summary: {{ post.summary }}</li>
    {% endfor %}
  </ul>
{% else %}
  <p>no post</p>
{% endif %}
```