def anagrams(word, words):
    words1 = words.copy()
    for element in words1:
        n = list(word)
        for letter in element:
            if letter in n:
                n.remove(letter)
        if len(n) != 0 or len(element) != len(word):
            words.remove(element)
    return(words)