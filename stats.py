def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def get_num_words():
    book_text = get_book_text("books/frankenstein.txt")
    list_of_words = book_text.split()
    number = len(list_of_words)
    print(f"{number} words found in the document")