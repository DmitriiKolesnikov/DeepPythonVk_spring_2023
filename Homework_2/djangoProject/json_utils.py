import json
FSON_FILE = 'djangoProject/bfm.jsonl'


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





