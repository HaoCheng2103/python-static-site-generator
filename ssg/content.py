import re
from yaml import load 
from _collections_abc import Mapping


class Content(Mapping):
    __delimeter = r"^(?:-|\+){3}\s*$"
    __regex = re.compile(__delimeter, re.MULTILINE)


    @classmethod
    def load(cls, string):
        _, fm, content = __regex.split(string, 2)

    
    def __init__(self, metadata, content):
        self.data = metadata
        self.data["content"] = content


    @property
    def body(self):
        return self.data["content"]
    

    @property
    def type(self):
        if "type" in self.data:
            return self.data["type"]
        else:
            return None


    @type.setter
    def type(self, type):
        self.data["type"] = type


    def __getitem__(self, __key):
        return self.data[__key]
    

    def __iter__(self):
        return self.data.__iter__
    

    def __len__(self):
        return len(self.data)
    

    def __repr__(self):
        data = {}
        for key, value in self.data.items():
            if key != "content":
                data[key] = value
        return str(data)
    
