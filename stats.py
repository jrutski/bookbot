def get_word_count(input):
    num_words = len(input.split())
    return num_words

def get_char_count(input):
    chars_dict = {}
    for letter in input:
        if not letter.lower() in chars_dict:
            chars_dict[letter.lower()] = 1
        else:
            chars_dict[letter.lower()] += 1
    return chars_dict

def sort_on(dict):
    return dict["num"]

def to_list(input):
    new_list = []
    for letter in input:
        count = input[letter]
        new_list.append({"char": letter, "num": count})
    new_list.sort(reverse=True, key=sort_on)
    return new_list