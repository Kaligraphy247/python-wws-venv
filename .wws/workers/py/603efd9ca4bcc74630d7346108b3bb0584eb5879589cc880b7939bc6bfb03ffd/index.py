from poly import *

"""A package that contains models that represent entities.
"""


res = worker(Request(json.loads(sys.stdin.read())))
print(res.to_json())
