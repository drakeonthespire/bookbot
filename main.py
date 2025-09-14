from stats import get_character_counts, get_num_words
import sys

def main():
    if sys.argv and len(sys.argv) > 1:
        book_path = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    word_count, char_dict = anaylize_book(book_path)
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    print(type(char_dict))
    sorted_by_count = sorted(char_dict, key=char_dict.get, reverse=True)
    
    for char in sorted_by_count:
        print(f"{char}: {char_dict[char]}")

def anaylize_book(book_path):

        
    word_count = get_num_words(book_path)
    char_dict = get_character_counts(book_path)
    return word_count, char_dict

    

if __name__ == "__main__":
    main()