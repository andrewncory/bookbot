import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    book_path = sys.argv[1]

def main():
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    the_counts = get_characters(text)
    sorted_chars = order_characters(the_counts)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["num"]
        if char.isalpha():
            print(f"{char}: {count}")
    
    print("============= END ===============")


def get_book_text(path):
    with open(path) as f:
        return f.read()


from stats import get_num_words

from stats import get_characters

from stats import order_characters

from stats import sort_on

main()

