from poly import *

# from sample import process_request_body


def worker(request):
	# data = process_request_body(request_body=request.body)
	# name = data["name"]
	# age = data.get("age")
	
	html = rf"""
	<!DOCTYPE html>
	<html lang="en">

	<head>
	<meta charset="UTF-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>WWS</title>
	</head>

	<body>
	<h1>Python WWS</h1>
	<form method="post">
		<label for="">Name</label>
		<input type="text" name="name">
		<label for="">Age</label>
		<input type="text" name="age">
		<button>Send</button>
	</form>

	</body>

	</html>
	"""
	res = Response(html)
	return res



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

res = worker(Request(json.loads(sys.stdin.read())))
print(res.to_json())
