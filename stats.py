def get_num_words(book_text):

    word_count = len(book_text.split())

    return word_count

def get_character_count(book_text):
    letter_count = {}
    characters = list(book_text.lower())
    for char in characters:
        if char not in letter_count:
            char_count = characters.count(char)
            letter_count[char] = char_count
    return letter_count

def dict_to_list_of_dicts(dict):
    count_list = []

    for char, count in dict.items():
        if char.isalpha():
            count_list.append({"char": char, "count": count})

    count_list.sort(reverse=True, key=sort_on)

    return count_list

def sort_on(dict):
    return dict["count"]
 