from collections import Counter

def main():
    bookpath = "books/frankenstein.txt"
    get_book_report(bookpath)



def get_book_text(path: str) -> str:
    with open(path) as f:
        text = f.read()
    
    return text

def get_word_count(booktext: str) -> int:
    words = booktext.split()
    return len(words)

def get_char_counts(booktext: str) -> dict:

    counter = Counter(booktext.replace(" ", "").lower())
    return dict(counter)

def get_book_report(bookpath: str):

    booktext = get_book_text(bookpath)
    
    # Get stats 
    word_count = get_word_count(booktext)
    char_counts = get_char_counts(booktext)
    sorted_chars = sorted(char_counts, key=lambda x: char_counts[x], reverse=True)

    # Generate report
    print(f"------------------------------Begin Report------------------------------")
    print(f"{word_count} words found in {bookpath.split('/')[-1]}", end="\n\n")

    [print(f"The '{char}' character was found {char_counts[char]} times") for char in sorted_chars if char.isalpha()]
    print(f"------------------------------End Report------------------------------")




main() 
