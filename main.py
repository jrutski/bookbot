from stats import get_word_count, get_char_count, to_list

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    file_path = "books/frankenstein.txt"
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print(f"----------- Word Count ----------")
    print(f"Found {get_word_count(get_book_text(file_path))} total words")
    print(f"--------- Character Count -------")
    new_list = to_list(get_char_count(get_book_text(file_path)))
    for dict in new_list:
        if dict['char'].isalpha(): print(f"{dict['char']}: {dict['num']}")
    print(f"============= END ===============")

main()
