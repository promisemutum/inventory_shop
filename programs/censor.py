sentence = input("Enter the sentence: ")
bad_words = ["fuck", "bitch", "hoe"]

def censor(words):
    length = len(words)
    star_temp = "*"*length
    return star_temp

for words in sentence.split():
    for temp in bad_words:
        if temp == words:
            words = censor(words)
    print(words + " ", end = " ")







