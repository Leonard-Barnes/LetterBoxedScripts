import sys

def invalid_options(set1, set2, set3, word):
    for i in range(len(word)-1):
        if word[i] not in set1 and word[i] not in set2 and word[i] not in set3:
            if word[i+1] not in set1 and word[i+1] not in set2 and word[i+1] not in set3:
                return True
    return False

def isValidSolution(string, letters):
    for letter in letters:
        if letter in string:
            continue
        else:
            return False
    return True

file = open("words.txt")
wordset = []
for line in file:
    wordset.append(line.strip())

set1 = sys.argv[1]
set2 = sys.argv[2]
set3 = sys.argv[3]
set4 = sys.argv[4]
wordset = sorted(wordset)
wordset.append("burqa")

letters = []
for letter in "abcdefghijklmnopqrstuvwxyz":
    if letter in set1 or letter in  set2 or letter in set3 or letter in set4:
        letters.append(letter)
print(letters)
goodwords = []

for word in wordset:
    if all([i in letters for i in word]) and len(word) > 1:
        goodwords.append(word)

finalwords = []

for word in goodwords:
    if (invalid_options(set1, set2, set3, word)):
        continue
    elif (invalid_options(set1, set2, set4, word)):
        continue
    elif (invalid_options(set1, set4, set3, word)):
        continue
    elif (invalid_options(set4, set2, set3, word)):
        continue
    else:
        finalwords.append(word)
       
for firstword in finalwords:
    for secondword in finalwords:
        if firstword[-1] == secondword[0]:
            if(isValidSolution(firstword + secondword, letters)):
                print(firstword + " " + secondword)
