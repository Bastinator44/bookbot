from stats import *


def get_book_text (file):
    with open(file, "r") as f:
        text = f.read()
    return(text)

def main ():
    text = get_book_text("./books/frankenstein.txt")
    get_num_words(text)
    character_count(text)
    
main()