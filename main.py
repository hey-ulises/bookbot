import sys
from stats import get_num_words, get_chars_count,sort_dict

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()

def main():
    filepath = sys.argv[1]
    book = get_book_text(filepath)
    num_words = get_num_words(book)
    num_chars = get_chars_count(book)
    sorted_chars = sort_dict(num_chars)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("---------- Word Count -----------")
    print(f"Found {num_words} total words")
    print("-------- Character Count --------")
    
    for char in sorted_chars:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")

main()