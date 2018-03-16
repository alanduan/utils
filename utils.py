import json

class DictionaryObject:
    def __init__(self, dictionary=None):
        if dictionary:
            self.__dict__.update(dictionary)
    def __setitem__(self, key, name):
        self.__dict__[key] = name
    def __getitem__(self, key):
        return self.__dict__[key]
    def __repr__(self):
        return repr(self.__dict__)
    def __str__(self):
        return str(self.__dict__)
    def to_json(self):
        return self.__dict__

class JsonEncoder(json.JSONEncoder):
    def default(self, o):
        if hasattr(o, 'to_json'):
            return o.to_json()
        return super().default(o)

magic = DictionaryObject(dict(key_0 = 42, key_1 = 'hello world'))
print(json.dumps(magic, cls=JsonEncoder, indent=2))
