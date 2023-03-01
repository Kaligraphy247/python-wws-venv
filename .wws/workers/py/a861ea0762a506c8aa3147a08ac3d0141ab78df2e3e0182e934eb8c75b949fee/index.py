from poly import *

"""Subpackage containing all of pip's command line interface related code
"""

# This file intentionally does not import submodules


res = worker(Request(json.loads(sys.stdin.read())))
print(res.to_json())
