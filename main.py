def get_book_text(filepath):
	with open(filepath) as f:
		return f.read()


def main():
	book_text = get_book_text("books/frankenstein.txt")
	from stats import words, characters, sort_list
	num_words = words(book_text)
	character = characters(book_text)
	sorted_chars = sort_list(character)
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at books/frankenstein.txt...")
	print("----------- Word Count ----------")
	print(f"Found {num_words} total words")
	print("--------- Character Count -------")
	for char_dict in sorted_chars:
		char = char_dict["char"]
		if char.isalpha():
			print(f"{char}: {char_dict['num']}")
	print("============= END ===============")

main()

