import json


FSON_FILE = '/Users/jimsgood/PycharmProjects/DeepPython_spring_2023/hw.jsonl'


def load_lib():
    docs = []
    with open(FSON_FILE, 'r') as ifd:
        for line in ifd:
            doc = json.loads(line.strip()) #получаем джецсоновское представление
            docs.append(doc)
        return docs


def search(pattern):
    docs = load_lib()
    res = []
    pattern = pattern.lower()
    for doc in docs:
        if 'title' in doc and pattern in doc['title'].lower():
            res.append(doc)
    return res

print(load_lib())
print(search("москве"))


def search_title(request):
    print(request)
    print(request.GET)
    w = request.GET['q']
    print(w)
    # results = {}
    # results['results'] = search(w)
    text_html = f'Search results for q ={w}'
    text_html += f' '
    for doc in search(w):
        text_html += f"{doc['title']}"
    text_html += ' '
    return text_html


print(load_lib())
