from django.shortcuts import render, HttpResponse

# Create your views here.


def list(request):   # user/list/ 
    return HttpResponse(f'''
        <div>{request.method}</div>
        <div>{request.path}</div>        
    ''')