from collections import Counter

def get_book_text(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: The file at {filepath} was not found.")
        return None
    except IOError:
        print(f"Error: An IOError occurred while trying to read the file at {filepath}.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
    
def get_num_words(document_path):
        content = get_book_text(document_path)
        word_count = len(content.split())
        return word_count

def get_character_counts(document_path):
    content = get_book_text(document_path).lower()

    return Counter(content)