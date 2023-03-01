from poly import *

#

def worker(request):
    return Response("Hello world from Python WWS")



res = worker(Request(json.loads(sys.stdin.read())))
print(res.to_json())
