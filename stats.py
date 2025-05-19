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


def sort_on(dict):
	return dict["num"]
def sort_list(char_dict):
	sorted_list = []
	for char, count in char_dict.items():
		sort = {"char": char, "num": count}
		sorted_list.append(sort)
	sorted_list.sort(reverse = True, key = sort_on)
	return sorted_list



