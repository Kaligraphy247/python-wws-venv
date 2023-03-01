from poly import *

from sample import process_request_body


def worker(request):
	data = process_request_body(request_body=request.body)
	name = data["name"]
	age = data.get("age")
	
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
	{request.body}
	{data}
	<h3>Data from Form</h3>
	Name: {name}
	Age: {age}
	</body>

	</html>
	"""
	res = Response(html)
	return res


res = worker(Request(json.loads(sys.stdin.read())))
print(res.to_json())
