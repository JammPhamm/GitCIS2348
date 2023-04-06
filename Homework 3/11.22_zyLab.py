#Pham, James 11.22 zyLab
# Input words
Words = input("")
# Convert words to list of words
ListOfWords = Words.split()

wordsFreq = {}  # Create an empty dictionary wordsFreq

# For loop run from 0 to length of ListOfWords - 1
for i in range(0, len(ListOfWords)):
    word = ListOfWords[i]
    if word not in wordsFreq:  # check if word is not in dictionary wordsFreq
        wordsFreq[word] = 1  # Assign frequency 1 to that word
    else:  # Otherwise
        wordsFreq[word] = wordsFreq[word] + 1  # Increment frequency of word by 1

# for loop run from 0 to length of ListOfWords - 1
for i in range(0, len(ListOfWords)):
    print(ListOfWords[i], wordsFreq[ListOfWords[i]])  # Display word and their frequency