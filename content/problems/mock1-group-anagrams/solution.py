def group_anagrams(words):
    groups = {}                               # sorted letters -> words with those letters
    for word in words:
        key = "".join(sorted(word))           # every anagram of word has the same key
        groups.setdefault(key, []).append(word)
    return list(groups.values())
