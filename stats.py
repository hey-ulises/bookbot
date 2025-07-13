def get_num_words(str):
    return len(str.split())

def get_chars_count(str):
    characters = {}

    for char in str:
        curr_char = char.lower()
        if curr_char not in characters:
            characters[curr_char] = 0
        characters[curr_char] += 1
    
    return characters

def sort_on(items):
    return items["num"]

def sort_dict(dict):
    sorted_chars = []

    for el in dict:
        sorted_chars.append({
            "char": el,
            "num": dict[el]
        })

    sorted_chars.sort(reverse=True, key=sort_on)

    return sorted_chars