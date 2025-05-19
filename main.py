import sys
def get_book_text(filepath):
	with open(filepath) as f:
		return f.read()


def main():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	else:
		book_text = get_book_text(sys.argv[1])
		from stats import words, characters, sort_list
		num_words = words(book_text)
		character = characters(book_text)
		sorted_chars = sort_list(character)
		print("============ BOOKBOT ============")
		print(f"Analyzing book found at {sys.argv[1]}...")
		print("----------- Word Count ----------")
		print(f"Found {num_words} total words")
		print("--------- Character Count -------")
		for char_dict in sorted_chars:
			char = char_dict["char"]
			if char.isalpha():
				print(f"{char}: {char_dict['num']}")
		print("============= END ===============")

main()

