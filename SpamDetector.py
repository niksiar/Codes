"""  
Spam detector 

Some of the internet spams follow one of these patterns below:

-  A word that has more than 2 capital letters
- A letter in a word is repeated at least three or more times
-  There is no vowel (o-i-e-a-u) in that word
- Characters other than letters are used in the word

Write a program to print the number of spam words in the output by taking a sentence.

Input: Includes a string containing words separated by a space character.

Output: An integer is the number of words that follow the spam pattern.

"""
note1 = input() + ' '
note2 = note1
my_class = []
t = 0
spams = 0
corrects = 0
number_of_words = 0
letters = "abcdefghijklmnopqrstuvwxyz"
all_letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
uppercase = letters.upper()


for n in note1:
    t = 0
    TF = False
    number_of_uppercase = 0
    if n != ' ':
        my_class.append(n)
    elif n == ' ':
        # each word process
       ## print(my_class)
        number_of_words += 1
        # 1-VOWEL
        if ('a' not in my_class) and ('e' not in my_class) and ('i' not in my_class) and ('o' not in my_class) and (
                'u' not in my_class) and ('A' not in my_class) and ('E' not in my_class) and ('I' not in my_class) and ('O' not in my_class)\
                and ('U' not in my_class):
            spams = spams + 1
            TF = True
           ## print("THE NUMBER OF SPAMS IS:" + str(spams))
        # 2-Upper Case
        for n in uppercase:
            if n in my_class:
                number_of_uppercase = number_of_uppercase + 1
        if number_of_uppercase > 1:
            if TF == False:
                spams = spams + 1
                TF = True
           ## print("THE NUMBER OF SPAMS IS:" + str(spams))

        # 3-Same Letters
        for n in all_letters:
            same_letters = my_class.count(n)
            if same_letters >= 3:
                if TF == False:
                    spams = spams + 1
                    TF = True
              ##  print("THE NUMBER OF SPAMS IS:" + str(spams))

        # 4-non-letter characters:
        for n in my_class:
            if n in all_letters:
                continue
            else:
                if TF == False:
                    spams = spams + 1
                    TF = True
               ## print("THE NUMBER OF SPAMS IS:" + str(spams))





        my_class = []

print(spams)
## print("NUMBER OF SPAM WORDS IS: " + str(spams))
## print("NUMBER OF WORDS IS: " + str(number_of_words))
