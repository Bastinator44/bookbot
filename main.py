import stats

def get_book_text (file):
    with open(file, "r") as f:
        text = f.read()
    return(text)

def main ():
    text = get_book_text("./books/frankenstein.txt")
    stats.get_num_words(text)
    
main()