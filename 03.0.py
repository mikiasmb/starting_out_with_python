codes = {
	'A': '%', 'a': '9',
	'B': '@', 'b': '#',
	'C': '$', 'c': '1',
	'D': '^', 'd': '2',
	'E': '&', 'e': '3',
	'F': '*', 'f': '4',
	'G': '(', 'g': '5',
	'H': ')', 'h': '6',
	'I': '-', 'i': '7',
	'J': '_', 'j': '8',
	'K': '+', 'k': '=',
	'L': '{', 'l': '[',
	'M': '}', 'm': ']',
	'N': '|', 'n': '\\',
	'O': ':', 'o': ';',
	'P': '"', 'p': "'",
	'Q': '<', 'q': ',',
	'R': '>', 'r': '.',
	'S': '?', 's': '/',
	'T': '0', 't': '!',
	'U': '1', 'u': '2',
	'V': '3', 'v': '4',
	'W': '5', 'w': '6',
	'X': '7', 'x': '8',
	'Y': '9', 'y': '0',
	'Z': '~', 'z': '`'
}
infile = open("text1.txt", "r")
encrypted_file = open("encrypted_text.txt", "w")
all_content = infile.read().strip()
infile.close()

for line in all_content:
	for char in line:
		if char in codes:
			encrypted_file.write(codes[char])
		else:
			encrypted_file.write(char)

encrypted_file.close()
