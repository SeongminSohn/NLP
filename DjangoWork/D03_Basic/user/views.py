from django.shortcuts import render, HttpResponse
from django.http import JsonResponse

# Create your views here.


def list(request):   # user/list/ 
    return HttpResponse(f'''
        <div>{request.method}</div>
        <div>{request.path}</div>        
    ''')

# /user/delete?id=4
def delete(request):
    id = request.GET['id']  # GET방식 요청에서 'id' parameter 값을 읽어온다.
    return HttpResponse(f'''
        <div>
            <p>id: {id}</p>
        </div>
    ''')

def detail(request, id):  # url 경로의 parameter 를 view 함수의 매개변수로 명시하면 된다.
    return HttpResponse(f'''
        <h3>/user/detail/id/ 요청</h3>
        <div>
            <p>id: {id}</p>
        </div>
    ''')

# Python -> JSON 
def create(request):
    data = {'name': 'John', 'age': 34}
    data = {'arr': [10, 20, 30, 40]}
    return JsonResponse(data)

# Template 리턴 (*.html)
def func01(request):
    # render(request, template, context...)
    return render(request, 'page01.html')

def func02(request):
    context = {
        'title': "두번째 페이지",
        'summary': '템플릿',
    }
    return render(request, 'page02.html', context)

'''
변수2
템플릿 시스템은 변수의 속성에 접근하기 위해 dot-lookup 문법을 사용

예제의 {{ question.question_text }} 구문을 보면, 

Django는 
1. Dictionary lookup
   먼저 question 객체에 대해 사전형으로 탐색합니다. 
2. Attribute lookup
   탐색에 실패하게 되면 속성값으로 탐색합니다. 
3. List-index lookup
   만약 속성 탐색에도 실패한다면 리스트의 인덱스 탐색을 시도하게 됩니다.  
https://docs.djangoproject.com/ko/4.0/intro/tutorial03/#use-the-template-system
'''
def func03(request):
    context = {
        # dict
        'album' : {
            'song': '노래노래',
            'artist': '가수가수',
        },
    }
    return render(request, 'page03.html', context)