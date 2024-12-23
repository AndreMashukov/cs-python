# You'll be given two arrays of words. Your task? Find the unique words in the first array that can rearrange their letters to match at least one word in the second array. Like transforming 'cinema' into 'iceman'

def find_anagram_words(word_list1, word_list2):
    word_list2 = set(''.join(sorted(word)) for word in word_list2)
    anagrams = {word for word in word_list1 if ''.join(sorted(word)) in word_list2}
    return sorted(list(anagrams))



print(find_anagram_words(['cinema', 'iceman'], ['iceman', 'cinema'])) # should return ['cinema', 'iceman']
print(find_anagram_words(['test', 'stet'], ['tent', 'nett'])) # should return []
print(find_anagram_words(['hello', 'world'], ['dolly', 'sir'])) # should return []