from poly import *

"""For modules related to installing packages.
"""


res = worker(Request(json.loads(sys.stdin.read())))
print(res.to_json())
