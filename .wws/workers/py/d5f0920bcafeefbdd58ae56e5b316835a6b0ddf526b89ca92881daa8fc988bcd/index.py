from poly import *

import json

sample_data = "name=peter&age=23&wage=30,000"

def process_request_body(request_body: str) -> dict:
    """
    Helper function for this project.
    Converts request body to Python dict.
    """

    request_body_data = request_body.split("&")
    serialized_body = {}
    
    for data in request_body_data:
        d = data.split("=")
        serialized_body[d[0]] = d[1]
    
    return serialized_body


def serialize_body(request_body: str) -> json:
    """
    Serializes request body. It takes a request body string,
    converts to valid Python Dict, and then stringify as valid JSON.
    """

    request_body_data = request_body.split("&")
    serialized_body = {}
    
    for data in request_body_data:
        d = data.split("=")
        serialized_body[d[0]] = d[1]

    return json.dumps(serialized_body, indent=2)


def deserialize_body(json_data: json) -> dict:
    """
    Deserialize body data. It takes valid json and returns
    a Python dictionary.
    """
    return json.loads(json_data)


# * Test
# s = serialize_body(request_body=sample_data)
# print(s)
# d = deserialize_body(s)
# print(d.get("wage"))




res = worker(Request(json.loads(sys.stdin.read())))
print(res.to_json())
