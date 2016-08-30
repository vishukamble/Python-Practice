# __author__ = Vishu Kamble
"""
A python program to get 2 numbers in an array whose sum is equal to a value given
"""

def pair_sum(arr, value):
    if len(arr) < 2:
        return

    seen = set()
    output = set()

    for num in arr:
        target = value - num

        if target not in seen:
            seen.add(num)
        else:
            output.add( (min(num, target), max(num, target)) )

    print '\n'.join(map(str,list(output)))

    return len(output)

print pair_sum((1,2,6,3), 4)