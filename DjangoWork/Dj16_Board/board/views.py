from django.shortcuts import render, HttpResponse

# Create your views here.

def write(request):
    response = f'{request.path} {request.method}요청'
    print(response)
    return render(request, 'write.html')

def detail(request, id):
    response = f'{request.path} {request.method}요청, id:{id}'
    print(response)
    return render(request, 'detail.html')

def list(request):
    response = f'{request.path} {request.method}요청'
    print(response)
    return render(request, 'list.html')

def update(request, id=None):
    response = f'{request.path} {request.method}요청, id:{id}'
    print(response)
    return render(request, 'update.html')

def delete(request):
    response = f'{request.path} {request.method}요청'
    print(response)
    return HttpResponse(response)