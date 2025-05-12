def get_book_text(filepath): #get book text
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    text = get_book_text("books/frankenstein.txt")
    from stats import count_book_words
    num_words = count_book_words(text)
    print(f"{num_words} words found in the document")

main()