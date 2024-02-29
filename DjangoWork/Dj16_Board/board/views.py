from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from board.models import Post

# Create your views here.

@csrf_exempt
def write(request):
    response = f'{request.path} {request.method}요청'
    print(response)

    if request.method == "GET":
        return render(request, 'write.html')  # 글 작성 form
    elif request.method == "POST":
        # form 에서 넘어온 값들로 DB 에 저장
        user = request.POST['user']  # name='user'
        subject = request.POST['subject']
        content = request.POST['content']
        post = Post(user = user, subject = subject, content = content)
        post.save()   # INSERT, id 값이 설정!

        context = {
            "result": 1,
            "post": post,
        }
        return render(request, 'writeOk.html', context)



def detail(request, id):
    response = f'{request.path} {request.method}요청, id:{id}'
    print(response)

    post = Post.objects.get(id = id)  # SELECT, PK로 검색

    #조회수 증가
    post.view_cnt += 1
    post.save() # UPDATE

    return render(request, 'detail.html', {'post': post})

def list(request):
    response = f'{request.path} {request.method}요청'
    print(response)

    posts = Post.objects.order_by('-id')  # id 컬럼 역순으로 SELECT

    return render(request, 'list.html', {'list': posts})

@csrf_exempt
def update(request, id=None):
    response = f'{request.path} {request.method}요청, id:{id}'
    print(response)
    return render(request, 'update.html')

@csrf_exempt
def delete(request):
    response = f'{request.path} {request.method}요청'
    print(response)
    return HttpResponse(response)