#"Write a program that prints the numbers from 1 to 100.
#But for multiples of three print “Fizz” instead of the number
#and for the multiples of five print
#“Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”."

number = list(range(1,101))

for numout in number:
    if numout %3 ==0 and numout%5 ==0:
        print('Fizzbuzz')
    elif numout %3 ==0:
        print('Fizz')
    elif numout %5 ==0:
        print('Buzz')
    else:
        print (numout)
