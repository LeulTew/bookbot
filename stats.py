def get_num_words(text):
    # takes a string as input and returns the number of words in the string.
    return len(text.split())

def get_num_characters(text):
    # takes a string as input and returns the number of times each character, (including symbols and spaces)
    char_count = {}
    for char in text:
        char = char.lower()
        char_count[char] = char_count.get(char, 0) + 1
    return char_count

def sort_on(items):
    return items["num"]

def sort_characters(char_count):
    # Returns a sorted list of dicts: [{"char": ..., "num": ...}, ...], sorted by count descending
    char_list = [{"char": char, "num": count} for char, count in char_count.items()]
    char_list.sort(key=sort_on, reverse=True)
    return char_list
