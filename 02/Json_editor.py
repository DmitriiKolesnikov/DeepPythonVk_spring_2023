import json


def handle_name(name, value):
    print(f"Found name '{name}' with value '{value}'")


def process_json(json_str, fields, names, name_handler):
    data = json.loads(json_str)
    for field in fields:
        if field in data:
            for item in filter(None, (d.get(names[0]) for d in data[field])):
                for name in names[1:]:
                    item = item.get(name)
                    if not item:
                        break
                else:
                    name_handler(names[-1], item)


json_str = '''
{
    "people": [
        {"name": "John", "age": 30},
        {"name": "Alice", "age": 25}
    ]
}
'''

fields = ['people']
names = ['name']
process_json(json_str, fields, names, handle_name)
