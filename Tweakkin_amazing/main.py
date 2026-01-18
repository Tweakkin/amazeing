import sys

if __name__ == "__main__":
	if len(sys.argv) < 2:
		print("Error: Missing configuration file.")
		sys.exit(1)
	with open(sys.argv[1], "r") as file:
		parsed_dict = {}
		for line in file:
			line = line.strip()
			if not line[0] == '#':
				line = line.split(sep='=', maxsplit=1)
				parsed_dict.update({line[0].strip() : line[1].strip()})
		print(parsed_dict)

#testing git