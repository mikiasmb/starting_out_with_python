try:
	file1name = input("Enter first file name (without extension): ") + ".txt"
	file2name = input("Enter second file name (without extension): ") + ".txt"

	with open(file1name, "r") as file1, open(file2name, "r") as file2:
		content1 = file1.read().strip().split()
		content2 = file2.read().strip().split()

	if not content1:
		print(f"The file {file1name}.txt is empty.")
	if not content2:
		print(f"The file {file2name}.txt is empty.")
	if content1 and content2:
		unique_words1 = set(w for w in content1)
		unique_words2 = set(w for w in content2)
		
		print(f"List of unique words contained in both files: {unique_words1 | unique_words2}")  # | -> union
		print(f"List of words that appears in both files: {unique_words1 & unique_words2}")  # & -> intersection
		print(f"List of words that appears in {file1name} but not in {file2name}: {unique_words1 - unique_words2}")
		print(f"List of words that appears in {file2name} but not in {file1name}: {unique_words2 - unique_words1}")
		print(f"""List of the words that appear in either the first or second file, but not both:
	{unique_words1 ^ unique_words2}""")  # ^ -> symmetric difference

except FileNotFoundError:
	print("Error! One or both files are not found. Please check the file names and try again.")
