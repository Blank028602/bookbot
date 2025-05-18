def words(book_text):
        num_words = 0
        for i in book_text.split():
                num_words += 1
        return num_words
def characters(book_text):
	character = {}
	for i in book_text:
		i = i.lower()
		if i in character:
			character[i] += 1
		else: 
			character[i] = 1
	return character

