def count_book_words(text):
    words = text.split()
    return len(words)

def count_char(text):
    char = {}
    for letter in text:
        letter_lower = letter.lower()
        if letter_lower in char:
            char[letter_lower] += 1
        else:
            char[letter_lower] = 1
    return char

def sort_char_counts(char_dict):
    char_list = []
    for char, count in char_dict.items():
        char_list.append({"char": char, "num": count})

    def sort_on(dict_item):
        return dict_item["num"]
    
    char_list.sort(reverse=True, key=sort_on)
    return char_list