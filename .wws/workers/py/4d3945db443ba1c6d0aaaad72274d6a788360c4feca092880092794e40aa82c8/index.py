from poly import *

# from sample import process_request_body


def worker(request):

	
	# data = process_request_body(request_body=request.body)
	data = str("Hi")
	# name = data["name"]
	# age = data.get("age")
	x = lambda : "Hello World"

	# * This lambda function takes a string, and converts it into a python dict, 
	# * Here, the function is spread into multiple lines for readability.
	prb = (lambda body: 
		{key.split("=")[0]: value.split("=")[1]
		for (key, value) in zip(body.split("&"), body.split("&"))}
		) #(sample_data) #? the previous comment is for IIFE
		
	x = lambda : "hello"


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
	{data}
	{x()}
	</body>

	</html>
	"""
	res = Response(html)
	return res



# def process_request_body(request_body: str) -> dict:
# 	"""
# 	Helper function for this project.
# 	Converts request body to Python dict.
# 	"""

# 	request_body_data = str(request_body.split("&"))
# 	serialized_body = {}
	
# 	for data in request_body_data:
# 		d = data.split("=")
# 		serialized_body[d[0]] = d[1]
	
# 	return serialized_body	




# https://www.learnbyexample.org/python-lambda-function/

res = worker(Request(json.loads(sys.stdin.read())))
print(res.to_json())
