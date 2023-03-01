from poly import *



res = worker(Request(json.loads(sys.stdin.read())))
print(res.to_json())
