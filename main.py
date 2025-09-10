from stats import get_character_counts, get_num_words


def main():
    book_path = "./books/frankenstein.txt"
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
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