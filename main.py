from stats import *
import sys

def get_file ():
    if len(sys.argv) == 1:
        print(sys.argv[1])
        return(sys.argv[1])
    else:
        sys.exit(1)

def get_book_text (file):
    with open(file, "r") as f:
        text = f.read()
    return(text)

def main ():
    text = get_book_text(get_file())
    
    num_words = get_num_words(text)
    #print(f"{num_words} words found in the document")
    
    char_counts = character_count(text)
    #print(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char, count in char_counts.items():
        print(f"{char}: {count}")
    print("============= END ===============")

main()