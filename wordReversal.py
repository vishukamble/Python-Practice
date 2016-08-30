# __author__ = Vishu Kamble
"""
A python program to reverse words in a sentence
"""

def wordReverse(sentence):
    print ' '.join(reversed(sentence.split(' ')))

def wordReverse2(sentence):
    words = []
    sentence = str(sentence).split(' ')
    length = x = len(sentence)
    for i in range(length):
        words.append(sentence[x-1])
        x -= 1

    print ' '.join(words)

wordReverse("Hey Hello How do you do")
wordReverse2("Hey Hello How do you do")