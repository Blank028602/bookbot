def get_book_text(filepath):
	with open(filepath) as f:
		return f.read()


def main():
	book_text = get_book_text("books/frankenstein.txt")
	from stats import words
	num_words = words(book_text)
	from stats import characters
	character = characters(book_text)
	print(f"{num_words} words found in the document")
	print(character)

main()

