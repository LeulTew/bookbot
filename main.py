from stats import get_num_characters, get_num_words, sort_characters
import sys

def get_book_text(path):
    with open(path) as file:
        return file.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    try:
        print("============ BOOKBOT ============\n")
        print(f"Analyzing book found at {book_path}...\n")
        book_text = get_book_text(book_path)
        char_count = get_num_characters(book_text)
        print("----------- Word Count ----------")
        print(f"Found {get_num_words(book_text)} total words\n")
        print("--------- Character Count -------")
        sorted_chars = sort_characters(char_count)
        for item in sorted_chars:
            print(f"{item['char']}: {item['num']}")
        print()
    except FileNotFoundError:
        print(f"Error: The file at {book_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

main()