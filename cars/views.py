# from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def cars_view(request):
    #html temporário
    html = '''
    <html>
        <head>
            <title>Meus carros</title>
        </head>
        <body>
            <h1>Carros do Carlos</h1>
            <h3>Só carros top!</h3>
        </body>
    </html>
    '''
    return HttpResponse(html)
    # return HttpResponse('<h1>Meus carros testes</h1>')
