def get_num_words (text):
    num_words = len(text.split())
    print(f"{num_words} words found in the document")
    return(num_words)

def character_count(text):
    char_counts = {}
    lowered_text = text.lower()
    for char in lowered_text:
        if char.isalpha():
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1
    print(char_counts)