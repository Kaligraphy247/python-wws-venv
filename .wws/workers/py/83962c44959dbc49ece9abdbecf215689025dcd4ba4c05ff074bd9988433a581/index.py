from poly import *

SUCCESS = 0
ERROR = 1
UNKNOWN_ERROR = 2
VIRTUALENV_NOT_FOUND = 3
PREVIOUS_BUILD_DIR_ERROR = 4
NO_MATCHES_FOUND = 23


res = worker(Request(json.loads(sys.stdin.read())))
print(res.to_json())
