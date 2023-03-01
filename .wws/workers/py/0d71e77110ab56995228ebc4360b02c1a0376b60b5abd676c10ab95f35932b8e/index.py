from poly import *

#


def worker(request):
    with open("file.html", "r") as file:
        ext_file = file.read()
    # return Response("Hello world from Python WWS")
    return Response(ext_file)


# with open("file.html", "r") as file:
#     print(file)


res = worker(Request(json.loads(sys.stdin.read())))
print(res.to_json())
