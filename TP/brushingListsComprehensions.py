# __author__ = Vishu Kamble
"""
A python program to 
"""
st = "Print every word in this sentence that has an even number of letters"
lst = [letter for letter in st.split(' ') if len(letter) % 2 == 0]
print lst

st1 = "Create a list of the first letters of every word in this string"
l = [first[0] for first in st1.split()]
print l

st2 = "Print only words that starts with s in this sentence."
l1 = [s for s in st2.split() if s[0] == 's']
print l1

# Number divisible by 3
l3 = [x for x in range(1, 50) if x % 3 == 0]
print l3
