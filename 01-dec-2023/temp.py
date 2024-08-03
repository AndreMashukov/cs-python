import re
from collections import defaultdict

def rare_words_finder(text):
    # implement this
    words = text.lower().split()
    word_counts = defaultdict(int)
    
    for word in words:
        word_counts[word] += 1
        
    rarest_words = []
    max_count = float('inf')
    for word, count in word_counts.items():
        if count < max_count:
            rarest_words = [(word, count)]
            max_count = count
        elif count == max_count:
            rarest_words.append((word, count))
    #limit the output to only five words.
    return rarest_words[:5]

print(rare_words_finder("Hey there hot shot Are you ready for a challenge This might be trickier than it looks")) # Expected Output: [('hey', 1), ('there', 1), ('hot', 1), ('shot', 1), ('are', 1)]

print(rare_words_finder("The quick brown fox jumps over the lazy dog The fox is quick but the dog is lazy")) # Expected Output: [('brown', 1), ('jumps', 1), ('over', 1), ('but', 1), ('is', 2)]

print(rare_words_finder("")) # Expected Output: []