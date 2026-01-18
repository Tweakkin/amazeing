import sys

if __name__ == "__main__":
	# sys.argv must contain exactly 2 items: [script_name, config_file]
	if len(sys.argv) != 2:
		print("Error: Usage is python3 main.py <config_file>")
		sys.exit(1)
	try:
		#using 'with' to always close the file
		with open(sys.argv[1], "r") as file:
			parsed_dict = {}
			#looping through lines of the file
			for line in file:
				#removing white spaces at the beggining and end of file
				line = line.strip()
				#skipping the line if its empty
				if not line:
					continue
				#skipping the line if its a comment
				if line.startswith('#'):
					continue
				#splitting when first '=' is found
				line = line.split(sep='=', maxsplit=1)
				#adding result to the dict
				parsed_dict.update({line[0].strip() : line[1].strip()})
			print(parsed_dict)
	#handling if file was not found error
	except FileNotFoundError:
		print(f"Error: the file '{sys.argv[1]} was not found")
		sys.exit(1)
	#handling permission denied error
	except PermissionError:
		print(f"Error: you do not have permission to read '{sys.argv[1]}'")
		sys.exit(1)
