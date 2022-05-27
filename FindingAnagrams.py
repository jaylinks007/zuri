# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here

    word.lower()
    anagram.lower()

    #the sorted strings are checked

    if sorted(word)==sorted(anagram):
        return True
    else:
        return False

    # print(find_amagram('below', 'elbow')

    print(find_anagram(input('Type a word that is an anagram: \n'), input('Type a word that is an anagram of the first word: \n')))
