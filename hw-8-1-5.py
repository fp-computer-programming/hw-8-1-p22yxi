# Yongdong Xi

def palindrome():
    word = input("Give me a word: ")
    word2 = (word[::-1])
    if word == word2 :
        print(word2, 'is palindrome')


palindrome()
