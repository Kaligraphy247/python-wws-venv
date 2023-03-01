from poly import *

"""Contains purely network-related utilities.
"""


res = worker(Request(json.loads(sys.stdin.read())))
print(res.to_json())
