def get_book_text(filepath):
	with open(filepath) as f:
		return f.read()
def words(book_text):
	num_words = 0
	for i in book_text.split():
		num_words += 1
	return num_words


def main():
	book_text = get_book_text("books/frankenstein.txt")
	num_words = words(book_text)
	print(f"{num_words} words found in the document")

main()
