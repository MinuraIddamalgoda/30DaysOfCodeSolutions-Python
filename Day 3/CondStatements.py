# strip() takes off any whitespace from the beginning and end of a string.
# In this case, the string is the input the user enters (which will be converted
# to an integer afterwards). Strip() also has an optional parameter that
# takes off the specified character -- for example strip('a') would return
# "Hello world" if it was given "aaaaaaaHello Worldaaa" as an input.
N = int(input().strip())
    
if N % 2 != 0:
    print('Weird')
elif N % 2 == 0 and N >= 2 and N <= 5:
    print('Not Weird')
elif N % 2 == 0 and N >= 6 and N <= 20:
    print('Weird')
elif N % 2 == 0 and N > 20:
    print('Not Weird')
