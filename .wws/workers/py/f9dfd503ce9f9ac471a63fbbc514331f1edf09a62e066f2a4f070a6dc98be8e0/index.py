from poly import *

#


def worker(request):
    return Response("WEEE")


res = worker(Request(json.loads(sys.stdin.read())))
print(res.to_json())
