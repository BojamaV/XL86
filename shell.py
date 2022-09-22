import basic #imports main py file

while True:
	text = input('XL86 > ') 
	if text.strip() == "": continue
	result, error = basic.run('<si>', text)

	if error:
		print(error.as_string())
	elif result:
		if len(result.elements) == 1:
			print(repr(result.elements[0]))
		else:
			print(repr(result))
