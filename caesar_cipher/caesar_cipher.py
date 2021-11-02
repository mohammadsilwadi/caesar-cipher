import nltk, re
from nltk.corpus import words , names

nltk.download('words', quiet=True)
nltk.download('names', quiet=True)
word_list = words.words()
name_list = names.words()

def encrypt(m, k):
    offset = 65 # A
    offestb =97 # a
    words = m.split()
    cipher_words = []
    for word in words:
        cipher = ""
        for char in word:
            if ord(char)>=64 and ord(char)<= 90:
                char_num = ord(char.upper())
                shifted_num = char_num + k - offset
                mod_num = shifted_num % 26 + offset
                cipher += chr(mod_num)
            elif ord(char)>=97 and ord(char)<=122:
                char_num = ord(char.lower())
                shifted_num = char_num + k - offestb
                mod_num = shifted_num % 26 + offestb
                cipher += chr(mod_num)
            else :
               cipher += char 
        cipher_words.append(cipher)
    return " ".join(cipher_words)


def decrypt(encrypted,key):
    return encrypt(encrypted,-key)

def count_words(text):

    words = text.split()

    word_count = 0

    for candidate_word in words:
        word = re.sub(r'[^A-Za-z]+','', candidate_word)
        if word.lower() in word_list or word in name_list:
            word_count += 1

    return word_count

def crack(phrase): 
    for key in range(0,27):
        new_phrase = decrypt(phrase,key)
        word_count = count_words(new_phrase)
        percentage = int(word_count / len(phrase.split()) * 100)
        if percentage > 50:
            return(new_phrase)    