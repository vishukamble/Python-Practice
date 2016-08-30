# __author__ = Vishu Kamble
# """ A python program to find how many times a character is repeated in sing """

def compressed(s):
    length = len(s)
    result = ""
    if length == 0:
        return

    if length == 1:
        return s+"1"

    else:
        count = 1
        i = 1
        while i < length:

            if s[i] == s[i-1]:
                count += 1
            else:
                result += s[i-1] + str(count)
                count = 1

            i+=1

        result += s[i-1] + str(count)

    return result

print compressed("AAAABBBCCCCCDDDD")