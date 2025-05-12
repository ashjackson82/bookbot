import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

filepath = sys.argv[1] 

def get_book_text(filepath): #get book text
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

from stats import count_book_words, count_char, sort_char_counts


def main():
    text = get_book_text(filepath)

    num_words = count_book_words(text)
    char_counts = count_char(text)
    sorted_chars = sort_char_counts(char_counts)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char_item in sorted_chars:
        if char_item["char"].isalpha():
            print(f"{char_item['char']}: {char_item['num']}")
    print("============= END ===============")

if __name__ == "__main__":
    main()