def wordSplit(str1, list_words, output=None):
    if output is None:
        output = []

    for word in list_words:
        if str1.startswith(word):
            output.append(word)
            return wordSplit(str1[len(word):], list_words, output)

    return output

print wordSplit('iamprogramminginpython', ['you', 'am', 'i', 'dogs', 'python', 'in', 'programming'])