def find_unique_string(words):
    # implement this
    # words = [x.upper() for x in words]
    unique_words = []
    for word in words:
        if words.count(word) == 1:
            unique_words.append(word)
    # return " ".join(unique_words)
    # is to return only the last unique string from the list
    return len(unique_words) != 0 and unique_words[-1] or ''


print(find_unique_string(['apple', 'banana', 'apple', 'mango', 'banana']))  # It should print: 'mango'