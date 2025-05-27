def get_num_words (text):
    num_words = len(text.split())
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
    return(sorted_dict(char_counts))

def sorted_dict(d):
    items = sorted(d.items(), key=lambda item: item[1], reverse=True)
    return (dict(items))