from stats import get_num_words
from stats import get_character_count
from stats import dict_to_list_of_dicts
import sys

def get_book_text(fp): #takes a filepath
    with open(fp) as f:
        book_contents = f.read()
    return book_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(f"{sys.argv[1]}")
    num_words = get_num_words(book_text)
    char_count = get_character_count(book_text)
    sorted_count_list = dict_to_list_of_dicts(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dict in sorted_count_list:
        print(f"{dict['char']}: {dict['count']}")
    print("============= END ===============")
    return


main()