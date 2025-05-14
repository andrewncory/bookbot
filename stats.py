def get_num_words(text):
    words = text.split()
    return len(words)

def get_characters(text):
	character = text.lower()
	counts = {}
	for ch in character:
		if ch in counts:
			counts[ch] += 1
		else:
			counts[ch] = 1
	return counts

def order_characters(char_count):
	char_list = []
	for char, count in char_count.items():
		char_list.append({"char": char, "num": count})
	char_list.sort(reverse=True, key=sort_on)
	return char_list

def sort_on(dict):
    return dict["num"]
