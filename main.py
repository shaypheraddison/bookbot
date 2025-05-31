from stats import count_words, count_characters, sorted_list
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    num_words = count_words(sys.argv[1])
    counted_characters = sorted_list(sys.argv[1])
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char_dict in counted_characters:
        print(f"{char_dict['char']}: {char_dict['num']}")



print("============ BOOKBOT ============")
print(f"Analyzing book found at {sys.argv[1]}...")
main()