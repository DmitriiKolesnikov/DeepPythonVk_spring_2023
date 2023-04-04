from django.http import HttpResponse, JsonResponse
from .json_utils import search


def search_title(request):
    print(request)
    print(request.GET)
    w = request.GET['q']
    print(w)
    # results = {}
    # results['results'] = search(w)
    text_html = f'<h1>Search results for q ={w}</h1>'
    text_html += f'<ul>'
    for doc in search(w):
        text_html += f"<li>{doc['title']}</li>"
    text_html += '</ul>'
    return HttpResponse(text_html)

