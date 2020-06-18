
def find_anagrams(string, array):

    letter_dict = {}    # dictionary with each character of the given string and it's occurrence
    compare_dict = {}   # dictionary which gets compared to letter_dict for each word in given candidates
    anagrams = []       # the valid candidates to return

    for char in string.lower():
        if char not in letter_dict:
            letter_dict[char] = 0
        elif char in letter_dict:
            letter_dict[char] += 1

    for word in array:
        for char in word.lower():
            if char not in compare_dict:
                compare_dict[char] = 0
            elif char in letter_dict:
                compare_dict[char] += 1

        if letter_dict == compare_dict and word.lower() != string.lower():
            anagrams.append(word)
        compare_dict = {}

    return anagrams