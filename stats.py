def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()

    return file_contents


def count_words(filepath):
    text = str(get_book_text(filepath))
    split_text = text.split()
    count_text = len(split_text)

    return count_text

def count_characters(filepath):
    text = str(get_book_text(filepath)).lower()
    character_dict = {}
    for character in text:
        lower_case = character.lower()
        if lower_case not in character_dict:
            character_dict[character] = 1
        else:
            character_dict[character] += 1

    return character_dict

def sorted_list(filepath):
    dictionary = count_characters(filepath)

    def sort_on(dict):
        return dict["num"]

    list_of_dictionaries = []
    for item in dictionary:
        if item.isalpha():
            char_dict = {}
            char_dict["char"] = item
            char_dict["num"] = dictionary[item]
            list_of_dictionaries.append(char_dict)
    
    list_of_dictionaries.sort(reverse=True, key=sort_on)
    return list_of_dictionaries