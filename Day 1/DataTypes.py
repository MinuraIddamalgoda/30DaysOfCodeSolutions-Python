i = 4
d = 4.0
s = 'HackerRank'

# input() interprets what the user enters, however for the sake of error prevention, I've
# wrapped the input() method in their appropriate types
i2 = int(input())
d2 = float(input())
s2 = input()

i3 = i + i2
d3 = d + d2

# note that the third parameter in print() is only available on python3 and above. It makes
# combing different strings easier as it denotes what to use to separate the two strings you
# want to print. So in this case, I wanted to use a space to separate so I entered sep=' '
# however if I wanted to separate the strings with an underscore, I'd enter sep='_'
print(s, s2, sep=' ')
print(i3)
print(d3)
